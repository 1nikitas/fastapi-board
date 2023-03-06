import datetime
import calendar
def amount_of_every_day_getter():
    obj = calendar.Calendar()

    mondays = 0
    tuesdays = 0
    wednesdays = 0
    thusdays = 0
    fridays = 0
    saturdays = 0
    sundays = 0
    year, month = datetime.datetime.now().year, datetime.datetime.now().month
    # iterating with itermonthdays2
    for day, index in obj.itermonthdays2(year, month):

        if day != 0:
            print(day, index)
            if index == 0:
                mondays += 1
            elif index == 1:
                tuesdays += 1
            elif index == 2:
                wednesdays += 1
            elif index == 3:
                thusdays += 1
            elif index == 4:
                fridays += 1
            elif index == 5:
                saturdays += 1
            elif index == 6:
                sundays += 1

    print((mondays,tuesdays,wednesdays,thusdays,fridays,saturdays,sundays))
    return [mondays,tuesdays,wednesdays,thusdays,fridays,saturdays,sundays]

amount_of_every_day_getter()