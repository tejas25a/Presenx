import time
import calendar
t=time.localtime()
#print(t)
#print(t.tm_year,t.tm_mon)
monthName=calendar.month_name[t.tm_mon]
numberDays=calendar.monthrange(t.tm_year,t.tm_mon)[1]

