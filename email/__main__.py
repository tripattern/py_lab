import sys
import email_mailjet

def main():
    api_key = sys.argv[1]
    api_secret = sys.argv[2]
    to_address = sys.argv[3]
    from_address = sys.argv[4]
    custom_id = "NewsGathered"
    subject = "News you can use, maybe..."
    text_message = "Did you disable html emails?"
    html_message = "<h2>Hi, here is your news for the day! Can you use news from <a href='https://bbc.com/'>BBC</a></h2><br />Have a great day!"
    email_mailjet.send_email(api_key, api_secret, to_address, from_address, custom_id, subject, text_message, html_message)


if __name__ == '__main__':
    main()
