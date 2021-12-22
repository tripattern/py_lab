from mailjet_rest import Client


def send_email(api_key, api_secret, from_address, to_address, custom_id, subject, text_message, html_message):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": from_address,
                    "Name": "Acorns"
                },
                "To": [
                    {
                        "Email": to_address,
                        "Name": ""
                    }
                ],
                "Subject": subject,
                "TextPart": text_message,
                "HTMLPart": html_message,
                "CustomID": custom_id
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
