
def cal_date(year: str, month: str, day: str, hour: int = 23, min: int = 59, sec: str = "00") -> str:
    return f'{year}{month}{day}T{hour}{min}{sec}'
name = "Уведомление о ДЗ 1!"
time = cal_date("2023", "03", "01" )
comment = "ссылки на дз"

template = f"""BEGIN:VCALENDAR
CALSCALE:GREGORIAN
X-WR-CALNAME:invitation
BEGIN:VTIMEZONE
TZID:Europe/Moscow
BEGIN:STANDARD
TZOFFSETFROM:+1417
TZNAME:GMT+3
TZOFFSETTO:+1417
END:STANDARD
END:VTIMEZONE
BEGIN:VEVENT
DTEND;TZID=Europe/Moscow:{time}
TRANSP:OPAQUE
DTSTART;TZID=Europe/Moscow:{time}
DTSTAMP:20230226T155728Z
SUMMARY:{name}
SEQUENCE:1
DESCRIPTION:{comment}
BEGIN:VALARM
TRIGGER:-PT5H
DESCRIPTION:This is an event reminder
ACTION:DISPLAY
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
DESCRIPTION:This is an event reminder
ACTION:DISPLAY
END:VALARM
BEGIN:VALARM
TRIGGER:-PT1H
DESCRIPTION:This is an event reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

with open('invitaion.ics', 'w') as file:
    file.write(template)