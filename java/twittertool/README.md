To create a Twitter app, go to https://apps.twitter.com

Get the consumerKey and consumerSecret from there and put it in the twitter4j.properties as oauth.conumserKey and oauth.consumerKeySecret

Login with the following code, authorize the app, and get the accessToken and accessTokenSecret for the twitter4j.properties as oauth.accessToken and oauth.accessTokenSecret.

    // Login
    Twitter twitter = new TwitterFactory().getInstance();
    RequestToken requestToken = twitter.getOAuthRequestToken();
    System.out.println("Please visit this URL: " +
            requestToken.getAuthenticationURL());
    Scanner scanner = new Scanner(System.in);
    String pin = scanner.nextLine();
    AccessToken accessToken = twitter.getOAuthAccessToken(requestToken, pin);
    System.out.println(accessToken.getScreenName());
    System.out.println(accessToken.getToken());
    System.out.println(accessToken.getTokenSecret());