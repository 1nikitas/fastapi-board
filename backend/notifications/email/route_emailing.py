from celery import Celery
from fastapi import APIRouter
from starlette.templating import Jinja2Templates
from fastapi import Request
from notifications.email.email_sender import send_email_notification

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get('/notificate')
def notificate(request: Request):
    send_email_notification()
    return {'ok': "1" }