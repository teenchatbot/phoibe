import datetime
import pytz
from datetime import date
# these sets of functions just get all the time related crap


class time:
    def read_time():
        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S")
        proper_time = str("The time in UTC 6 is: " + str(now))
        return proper_time

    def read_date():
        datetoday = str(date.today())
        return datetoday

    def timez(timezone):
        timezones = datetime.datetime.now(pytz.timezone(timezone))
        timezonetime = timezones.strftime("%d/%m/%Y %H:%M:%S %Z %z")
        timezonestr = str(timezonetime)
        return timezonestr
