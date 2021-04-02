# -*- coding:utf-8 -*-
import datetime,time

print('{:=^50}'.format(" datetime.date "))
print(datetime.date.today())
print(datetime.date.today().year)
print(datetime.date(2019,1,20))
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.isoformat(datetime.date.today()))
print(datetime.date.isoweekday(datetime.date.today()))
print(datetime.date.weekday(datetime.date.today()))
print(datetime.date.today().timetuple())
print(datetime.date.today().strftime("%Y/%m/%d"))

print('{:=^50}'.format(" datetime.time "))
print(datetime.time(12,32,50))
print(datetime.time(12,32,50).isoformat())
print(datetime.time(12,32,50).strftime("%H hour:%M min:%S sec"))




print('{:=^50}'.format(" datetime.datetime "))

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time()))
