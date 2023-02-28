# from email.message import EmailMessage
# import smtplib
# from celery import Celery
# from celery.schedules import crontab
# from flower.app import Flower
#
REDIS_HOST = "redis://localhost"
# celery = Celery('notifications', broker=REDIS_HOST)
#
# celery.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'email_sender',
#         'schedule': 60.0
#     },
# }
#
# SMTP_HOST = "smtp.gmail.com"
# SMTP_PORT = 465
#
# SMTP_USER = "n.kiselev2002@gmail.com"
# SMTP_PASSWORD = "rmadxekcpagwsaci"
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
# send_email_notification()


