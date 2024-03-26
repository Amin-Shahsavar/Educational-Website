from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy

from decouple import config


def send_email(request, user):
    subject = "Verify Nikupen Account"
    message = f"Your code is "
    from_email = config('EMAIL_HOST_USER')
    to_email = user.email
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[to_email],
    )
