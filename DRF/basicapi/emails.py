from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
def send_otp_via_email(email):
    subject = 'Your Account verficiation Email'
    otp = random.randint(100000, 999999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()

def send_passreset_email(email,link):
    subject = 'Password reset Link'
    email_from = settings.EMAIL_HOST
    message = f'password reset link : {link}'
    send_mail(subject, message, email_from, [email])
