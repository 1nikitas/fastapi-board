import datetime
from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from tools.dates import amount_of_every_day_getter
from db.repository.clients import get_all_active_clients, get_money_by_day
from db.session import get_db

from tools.money import get_month_money


def get_current_month():
    """сделать проверку на Январь"""
    month_number = datetime.datetime.now().month - 1
    months = ["January", "February", "March",
              "April", "May", "June", "July",
              "August", "September", "October",
              "November", "December"]
    return months[month_number]


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/analytics")
def analytics(request: Request):
    return templates.TemplateResponse("analytics/analytics.html", {'request': request, "info": [1,2,3,4,5]})

@router.get('/analytics/month')
def month_clients(request: Request, db: Session = Depends(get_db)):
    expected_money = get_month_money(db=db)
    return templates.TemplateResponse("analytics/month_analytics.html", {'request': request, 'expected_money': expected_money})

