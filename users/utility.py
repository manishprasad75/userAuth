from .models import UserProfile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import uuid


def isvalid(context):
    if context.get('password') is None:
        msg = 'Password not Provided'
        return (False, msg)
    else:
        password = context['password'].strip()
        if len(password) < 8:
            msg = 'Length of password must be greater than 8 char'
            return (False, msg)

    email = context.get('email')

    if email is None:
        msg = "Email Not Provided"
        return (False, msg)

    if email is not None and len(email) > 0:
        email = email.strip()
        try:
            validate_email(email)
            valid_email = True
        except ValidationError:
            msg = "Email is not Valid!!"
            return (False, msg)
    return (True, " ")

def sendMessage1(subject, message, user_email, html_content):
    # import pdb
    # pdb.set_trace()
    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email, ]
    if subject and message and recipient_list:
        try:
            send_mail(subject, message, email_from, recipient_list, html_message=html_content)
        except Exception as e:
            print(e)
            msg = "Error: Make sure Email is Valid"
            return False, msg
        msg = "Alert: Successfully Send OTP, Check your Email"
        return True, msg
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        msg = "Error: Make sure Email is Valid"
        return False, msg

def sendMessage(user, otp):
    subject = "Email Verification"
    message = f'Thankyou {user}, for using our application. This means a lot for us. ' \
              f'<p>OTP</p><h1><strong>{otp.value}</strong></h1>'
    html_content = message
    message = strip_tags(html_content)
    (status, msg) = sendMessage1(subject, message, user.email, html_content)

    if not status:
        print(msg)
        return False
    else:
        return True

    # return redirect(request, 'varification.html', {'email': user.email, 'msg': msg, 'col': "info"})

def getOTPValue():
    value = uuid.uuid4().hex[:6].upper()
    return value