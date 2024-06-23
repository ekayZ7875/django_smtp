# myapp/views.py

from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError, SMTPException
import logging

logger = logging.getLogger(__name__)


def send_test_email(request):
    subject = "Test Email"
    message = "This is a test email sent from Django."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["recipient@example.com"]

    try:
        send_mail(subject, message, email_from, recipient_list)
    except BadHeaderError:
        logger.error("Invalid header found.")
        return HttpResponse("Invalid header found.")
    except SMTPException as e:
        logger.error("SMTP error occurred: %s", e)
        return HttpResponse(f"SMTP error occurred: {e}")
    except Exception as e:
        logger.error("An error occurred: %s", e)
        return HttpResponse(f"An error occurred: {e}")

    return HttpResponse("Email sent successfully")
