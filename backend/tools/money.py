import datetime

from sqlalchemy.orm import Session

from db.repository.clients import get_all_active_clients, get_money_by_day
from tools.dates import amount_of_every_day_getter


def get_month_money(db: Session):


    mondays, tuesdays, wednesdays, thusdays, fridays, saturdays, sundays = amount_of_every_day_getter()
    mondays_clients = get_money_by_day("Понедельник", db=db) if  get_money_by_day("Понедельник", db=db) else 0
    tuesdays_clients = get_money_by_day("Вторник", db=db) if  get_money_by_day("Вторник", db=db) else 0
    wednesdays_clients = get_money_by_day("Среда", db=db) if  get_money_by_day("Среда", db=db) else 0
    thusdays_clients = get_money_by_day("Четверг", db=db) if  get_money_by_day("Четверг", db=db) else 0
    fridays_clients = get_money_by_day("Пятница", db=db) if  get_money_by_day("Пятница", db=db) else 0
    saturdays_clients = get_money_by_day("Суббота", db=db) if  get_money_by_day("Суббота", db=db) else 0
    sundays_clients = get_money_by_day("Воскресенье", db=db) if  get_money_by_day("Воскресенье", db=db) else 0

    print(mondays , mondays_clients)
    print(tuesdays , tuesdays_clients)
    print(wednesdays , wednesdays_clients)
    print(thusdays , thusdays_clients)
    print(fridays , fridays_clients)
    print(saturdays , sundays_clients)
    print(sundays , saturdays_clients)


    all_money = mondays * mondays_clients + tuesdays * tuesdays_clients + \
                wednesdays * wednesdays_clients + thusdays * thusdays_clients + \
                fridays * fridays_clients + saturdays * sundays_clients + sundays * saturdays_clients
    return all_money