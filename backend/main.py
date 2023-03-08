
from redis import asyncio as aioredis
import uvicorn
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from apis.base import api_router
from core.config import settings
from db.base import Base
from db.session import engine
from db.utils import check_db_connected
from db.utils import check_db_disconnected
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from webapps.base import api_router as web_app_router
from notifications.telegram.bot import bot, dp
from aiogram import types, Dispatcher, Bot
from notifications.telegram.bot import TOKEN
REDIS_HOST = "redis://localhost:6379"
WEBHOOK_PATH = f'/bot/{TOKEN}'
WEBHOOK_URL = f'https://e2d3-212-45-15-105.eu.ngrok.io' + WEBHOOK_PATH
print(WEBHOOK_URL)
def include_router(app):
    app.include_router(api_router)
    app.include_router(web_app_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    create_tables()
    return app

app = start_application()

@app.on_event("startup")
async def app_startup():
    await check_db_connected()
    redis = aioredis.from_url(REDIS_HOST, encoding="ut8f", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )

@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)



@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)