from celery import Celery
from celery.schedules import crontab
from telegram.bot import bot
from asgiref.sync import async_to_sync
from telegram.keyboard import main_keyboard
app = Celery('tasks', broker='redis://127.0.0.1:6379')

async def message_send():
    await bot.send_message(582897416, "Привет", reply_markup=)

@app.task
def show():
    async_to_sync(message_send)()

app.conf.beat_schedule = {
    'task-name': {
        'task': 'celery_tasks.show',  # instead 'show'
        'schedule': 5.0 #crontab(hour=21, minute=14, day_of_week=6)

    },
}

app.conf.timezone = 'Europe/Moscow'