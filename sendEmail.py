import yagmail
import os
import sys
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('EMAIL_ADDRESS')


def send_email(file_path, recipient_email):
    
    subject = "Processed Images Zip file"
    body = "Please find the processed images attached."
    
    
    try:
            yag = yagmail.SMTP(sender_email)
            yag.send(
                to=recipient_email,
                subject=subject,
                contents=body,
                attachments=file_path
            )
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python sendEmail.py <folder_path> <recipient_email>')
        sys.exit(1)

    folder_path = sys.argv[1]
    recipient_email = sys.argv[2]
    
    if os.path.exists(folder_path):
        send_email(folder_path, recipient_email)
    else:
        print(f"Attachement not found: {folder_path}")