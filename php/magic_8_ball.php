<?php
/**
 * Magic 8-ball that will return a random response to a question.
 */
?>
<html>
<body>

<?php
if (isset($_POST['question'])):
    $possible_responses = [
        "Absolutely.",
        "Most likely.",
        "I can't tell.",
        "Not likely.",
        "No way.",
    ];
    $response = $possible_responses[rand(0, count($possible_responses)-1)];
?>
<p>
    <b>Question:</b> <?=htmlspecialchars($_POST['question'])?><br />
    <b>Answer:</b> <?=$response?>
</p>
<?php endif ?>

<form method="post">
    Ask a question:
    <input type="text" name="question" />
    <input type="submit" />
</form>

</body>
</html>