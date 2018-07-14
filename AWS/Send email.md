# python -m pip install awscli
# SES must be configured first from the AWS management site and verify your to emails

python3 -m awscli ses send-email --from myemail@gmail.com --destination file://destination.json --message file://message.json


destination.json
{
    "ToAddresses":  ["johndleon@gmail.com"],
    "CcAddresses":  ["johndleon@gmail.com"],
    "BccAddresses": []
}


message.json
{
    "Subject": {
        "Data": "Test email sent using the AWS CLI",
        "Charset": "UTF-8"
    },
    "Body": {
        "Text": {
            "Data": "This is the message body in text format.",
            "Charset": "UTF-8"
        },
        "Html": {
            "Data": "This message body contains HTML formatting. It can, for example, contain links like this one: <a class=\"ulink\" href=\"http://docs.aws.amazon.com/ses/latest/DeveloperGuide\" target=\"_blank\">Amazon SES Developer Guide</a>.",
            "Charset": "UTF-8"
        }
    }
}
