import datetime
from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

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
def month_analytics(request: Request):
    month = get_current_month()


