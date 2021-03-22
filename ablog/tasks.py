from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
# from ablog.models import User
from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
logger = get_task_logger(__name__)

@task(name='send_welcome_mail')
def send_welcome_mail(user_email, full_name):
    html_content = render_to_string("registration/email_body.html",{'title':'Welcome to My Blog!!!!','full_name':full_name})
    subject, from_email, to = 'Welcome to My Blog!!!!', settings.EMAIL_HOST_USER, user_email
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()



