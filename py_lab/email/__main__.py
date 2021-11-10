import sys
from mailjet_rest import Client
import os

def main():
    api_key = sys.argv[1]
    api_secret = sys.argv[2]
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": sys.argv[3],
                    "Name": "Acorns"
                },
                "To": [
                    {
                        "Email": sys.argv[4],
                        "Name": ""
                    }
                ],
                "Subject": "News you can use...",
                "TextPart": "Did you disable html emails?",
                "HTMLPart": "<h2>Hi, here is your news for the day! <a href='https://bbc.com/'>BBC</a></h2><br />Have a great day!",
                "CustomID": "NewsGathered"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print (result.status_code)
    print (result.json())


if __name__ == '__main__':
    main()
