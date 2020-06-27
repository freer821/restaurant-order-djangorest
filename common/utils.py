import random
import string

from django.core import mail

from config.settings import EMAIL_HOST_USER


def sendEmail(subject, html_content, to_email):
    with mail.get_connection() as connection:
        msg = mail.EmailMessage(
            subject, html_content, EMAIL_HOST_USER, [to_email],
            connection=connection,
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

def getRandomNo(keylength=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=keylength))
