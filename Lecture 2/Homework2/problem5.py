import time
import datetime
import calendar
my_bday=datetime.date(1995, 11, 12)
print(my_bday)
print("My bday year:", my_bday.year)
print("My bday month:", my_bday.month)
print("My bday day:", my_bday.day)
print(my_bday.weekday())
current_date=datetime.date.today()
my_next_bday=datetime.date(2019, 11, 12)
print(current_date)
timedelta= my_next_bday - current_date
print(timedelta)
cal_may=calendar.month(2017, 5)
print(cal_may)
tday=datetime.date.today()
print(tday)
timedelta1=datetime.timedelta(days=1)
timedelta2=datetime.timedelta(days=2)
timedelta3=datetime.timedelta(days=3)
yesterday=tday-timedelta1
print(yesterday)
current_time=datetime.datetime.today()
print(current_time)
print(yesterday + timedelta2)
print(yesterday - timedelta3)