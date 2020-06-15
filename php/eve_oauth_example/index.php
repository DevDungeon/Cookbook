<?php
/**
 * This self-contained application demonstrates
 * It will inspect code, verify with EVE, and authorize to get an access token.
 * It stores user details in the session so the login persists with the session.
 *
 * User is redirected to this page by EVE after they login with EVE.
 *
 * How to use:
 *   - Set up this page on a web server.
 *   - Register your app with EVE: https://developers.eveonline.com/applications
 *       - Provide this page as the callback URL.
 *       - Get the Client ID and Secret Key values to fill out below
 *   - Visit this page in the browser, click login/logout
 *       - User will be sent to EVE to login but redirect back here when complete
 *
 * ## Steps
 *
 * 1. POST to https://login.eveonline.com/oauth/token with the `code` provided by the EVE's callback here.
 * The post body can be JSON. E.g. with the HTTP header of `Content-Type: application/json`
 * and body of `{"grant_type":"authorization_code","code":"XXX"}`)
 * or URL encoded (e.g. with HTTP header of `Content-Type: application/x-www-form-urlencoded`
 * and body of `?grant_type=authorization_code&code=XXX`
 * The HTTP POST request must also include HTTP Basic authorization with our app's client id/secret key as user/pass.
 * E.g. with HTTP header `Authorization: Basic XXXX` where XXXX is the base-64 encoded `username:password` value.
 * The response will come back with json: access_token, token_type, expires_in, refresh_token.
 * The access_token is the critical piece that you need to interact with the EVE API.
 *
 * 2. Make a GET request to , post to https://login.eveonline.com/oauth/verify with the access token.
 * This will verify the access token is valid with EVE.
 * It will also return the character information so you can print the user's name to the screen and know their ID.
 * When making the request, send it with an `Authorization` header as a token bearer with the user's access token.
 * E.g. "Authorization: Bearer " . $users_eve_access_token
 *
 * 3. When the access token expires (20 minutes), refresh the login by following the same steps,
 * but instead of `grant_type=authorization_code` it will be `grant_type=refresh_token` along with `refresh_token=XXXX`
 *
 * ## References
 *
 * - EVE SSO step-by-step: https://developers.eveonline.com/blog/article/sso-to-authenticated-calls
 * - EVE Swagger UI: https://esi.evetech.net/ui/#/
 */
require_once('settings.php');

define('EVE_VERIFY_URL', EVE_LOGIN_SERVER_URL . '/oauth/verify');
define('EVE_AUTH_URL', EVE_LOGIN_SERVER_URL . '/oauth/token');
define('EVE_LOGIN_URL', EVE_LOGIN_SERVER_URL . '/oauth/authorize?response_type=code&redirect_uri=' . EVE_OAUTH_CALLBACK_URL . '&client_id=' . EVE_CLIENT_ID . '&scope=' . EVE_OAUTH_SCOPES);
define('EVE_SESSION_KEY_NAME', 'eve_character_data');
define('SELF_REDIRECT_URL', parse_url($_SERVER['REQUEST_URI'])['path']);

class EveCharacter
{
    // Returned from auth endpoint in exchange for code
    public $access_token = null;
    public $refresh_token = null;
    public $token_expiry = null; // Number of seconds until expires. E.g. 1199 (~20 minutes) Comes from auth and refresh responses. Generally not used. $expires_on is better to use.
    public $token_type = null; // This one also provided by verify endpoint. Is Character when first log in, Bearer when refreshing
    // Returned from the verify endpoint with character info
    public $id = null;
    public $name = null;
    public $expires_on = null; // Time token expires, ISO time string in UTC. E.g. `2020-05-16T00:49:58`
    public $scopes = null;
    public $character_owner_hash = null;
    public $intellectual_property = null;

    public static function load_character()
    {
        if (session_status() != PHP_SESSION_ACTIVE) {
            session_start(); // Character data is stored in session and we require it.
        }
        if (isset($_SESSION[EVE_SESSION_KEY_NAME])) {
            $character = $_SESSION[EVE_SESSION_KEY_NAME];
            if ($character->is_token_expired()) {
                $character->refresh_expired_token(); // If this errors...couldn't log in. TODO handle this
            }
            return $character;
        }
        return new EveCharacter(); // Empty anonymous character;
    }

    function refresh_expired_token()
    {
        $curler = curl_init(EVE_AUTH_URL);
        curl_setopt_array($curler, [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode(['refresh_token' => $this->refresh_token, 'grant_type' => 'refresh_token']),
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
                "Authorization: Basic " . base64_encode(EVE_CLIENT_ID . ':' . EVE_SECRET_KEY),
            ],
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_RETURNTRANSFER => true,
        ]);
        $raw_response = curl_exec($curler);
        curl_close($curler);

        $response = json_decode($raw_response);
        if (isset($response->error)) {
            die('Error: ' . $response->error . ' - ' . $response->error_description);  // TODO HANDLE
        }

        $this->access_token = $response->access_token;
        $this->refresh_token = $response->refresh_token;
        $this->token_type = $response->token_type;
        $this->token_expiry = $response->expires_in;
    }

    function is_token_expired()
    {
        if (strtotime($this->expires_on) - time() < 30) { // If token is within 30 seconds of expiring, let's trigger a refresh.
            return true;
        } else {
            return false;
        }
    }

    function isLoggedIn()
    {
        return $this->name != null;
    }

    /**
     * Provide a logout feature that will destroy the relevant session data
     */
    function logout()
    {
        unset($_SESSION[EVE_SESSION_KEY_NAME]);
        // Redirect back to self minus code minus logout in GET query to ensure no weird issues and cant bookmark it or ever land on it
        header('Location: ' . SELF_REDIRECT_URL);
        exit();
    }

    /**
     * If a `code` is received in the GET query, then it should have been a redirect from an EVE login.
     * Process OAuth callback, using the code to authenticate with EVE on the user's behalf and get an access+refresh token
     * Store the access token in the session for use on subsequent requests
     * Also fetch the character information and store that info too.
     * If it fails anywhere along the way, log then just redirect back to self without code in URL.
     *
     * @param $code
     */
    function login($code)
    {
        error_log('Running EVE login...');
        $this->authorize_with_eve($code);
        $this->fetch_character_info();
        $_SESSION[EVE_SESSION_KEY_NAME] = $this;
        header('Location: ' . SELF_REDIRECT_URL);
        exit();
    }


    /**
     * Send the `code` from the callback URL to EVE to get an access token
     *
     * @param $code
     */
    function authorize_with_eve($code)
    {
        // POST `code` from login redirect callback to EVE to try and get access token for user
        $curler = curl_init(EVE_AUTH_URL);
        curl_setopt_array($curler, [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode(['code' => $_GET['code'], 'grant_type' => 'authorization_code']),
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
                "Authorization: Basic " . base64_encode(EVE_CLIENT_ID . ':' . EVE_SECRET_KEY),
            ],
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_RETURNTRANSFER => true,
        ]);
        $raw_response = curl_exec($curler);
        curl_close($curler);

        $response = json_decode($raw_response);
        if (isset($response->error)) {
            die('Error: ' . $response->error . ' - ' . $response->error_description);  // TODO HANDLE
        }

        $this->access_token = $response->access_token;
        $this->refresh_token = $response->refresh_token;
        $this->token_type = $response->token_type;
        $this->token_expiry = $response->expires_in;
    }

    /**
     * Fetches character information like name and ID from EVE using the access token
     */
    function fetch_character_info()
    {
        $curler = curl_init(EVE_VERIFY_URL);
        curl_setopt_array($curler, [
            CURLOPT_HTTPHEADER => ["Authorization: Bearer " . $this->access_token],
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_RETURNTRANSFER => true,
        ]);
        $raw_response = curl_exec($curler);
        $response = json_decode($raw_response);
        curl_close($curler);
        if (isset($response->error)) {
            error_log('Error verifying access token');
            return;
        }
        if (!isset($response->CharacterID)) { // No error messages, just get empty response on error
            error_log('Error: no character id');
            return;
        } else {
            $this->id = $response->CharacterID;
            $this->name = $response->CharacterName;
            $this->expires_on = $response->ExpiresOn; // Is this any different from the token_expiry??
            $this->scopes = $response->Scopes;
            $this->token_type = $response->TokenType; // Different from token type received in first auth call?
            $this->character_owner_hash = $response->CharacterOwnerHash;
            $this->intellectual_property = $response->IntellectualProperty;
        }
    }
}


$character = EveCharacter::load_character(); // make this part of the constructor now instead of a static factory? actually the explicit factory is kind of nice. no hidden magic in constructor

// Logout if URL includes ?logout=true
if (isset($_GET['logout']) && $_GET['logout'] == 'true') {
    $character->logout();
}

// Login if URL includes `code`. It was redirected from an EVE login.
if (isset($_GET['code'])) {
    $character->login($_GET['code']);
}

?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script
            src="https://code.jquery.com/jquery-3.5.1.min.js"
            integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
            crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
            integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
            crossorigin="anonymous"></script>
</head>
<body>

<div class="container">

    <div class="row">

        <div class="card" style="width: 250px;">
            <?php if ($character->isLoggedIn()): ?>
                <img src="//image.eveonline.com/Character/<?= $character->id ?>_256.jpg" class="card-img-top"
                     alt="Portrait of <?= $character - name ?>" style="width: 100%"/><b><?= $character->name ?></b>
                <small><a
                            href="?logout=true">Logout</a></small>
            <?php endif ?>
            <div class="card-body">
                <div class="card-title">
                    <?php if ($character->isLoggedIn()): ?>
                        Welcome, <?= $character->name ?><br/>
                    <?php else: ?>
                        Anonymous
                    <?php endif ?>
                </div>
                <div class="card-body">
                    <?php if ($character->isLoggedIn()): ?>
                        Welcome, <?= $character->name ?><br/>
                        (killboardlink) (eve who link)<br/>
                        allow them to comment in guestbook (pdo sqlite::memory)
                        <a href="#" class="btn btn-primary">Click me</a>
                    <?php else: ?>
                        Please <a href="<?= EVE_LOGIN_URL ?>">log in with EVE Online</a> for full access.
                        <a href="<?= EVE_LOGIN_URL ?>">
                            <img src="https://web.ccpgamescdn.com/eveonlineassets/developers/eve-sso-login-white-large.png"/>
                        </a>
                    <?php endif ?>
                </div>
            </div>
        </div><!-- .card -->


    </div><!-- .row -->

</div><!-- .container -->

</body>
</html>
