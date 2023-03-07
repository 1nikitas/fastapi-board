from email.message import EmailMessage
import smtplib

import pytz
from celery import Celery, shared_task
from celery.schedules import crontab
from celery import shared_task
from celery.utils.log import get_task_logger

import celery










# celery.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
#
# celery.conf.timezone = 'UTC'
#
# # celery.conf.beat_schedule = {
# #     'add-every-30-seconds': {
# #         'task': 'email_sender',
# #         'schedule': 60.0
# #     },
# # }
#
# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, send_email_notification, name='add every 10')
#
#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
# celery.autodiscover_tasks()
# @celery.task
# def test(arg):
#     print(arg)
#
# @celery.task
# def add(x, y):
#     z = x + y
#     print(z)
#
# #
# SMTP_HOST = "smtp.gmail.com"
# SMTP_PORT = 465
#
# SMTP_USER = "n.kiselev2002@gmail.com"
# SMTP_PASSWORD = "nodopeqeookszgmn"
#
#
# def get_email_template(username: str = None):
#     email = EmailMessage()
#     email['Subject'] = "Приглашение"
#     email['From'] = SMTP_USER
#     email['To'] = SMTP_USER
#     email.set_content(
#         '<div>'
#         f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
#         '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
#         '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
#         '-mobile-free-vector.jpg" width="600">'
#         '</div>',
#         subtype='html'
#     )
#     return email
#
# @celery.task
# def send_email_notification(user: str = None):
#     email = get_email_template()
#     with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
#         server.login(SMTP_USER, SMTP_PASSWORD)
#         server.send_message(email)


#
#
#
