from persiantools.jdatetime import JalaliDateTime
import pytz
import jdatetime

day = jdatetime.datetime.now().day
month = jdatetime.datetime.now().month
year = jdatetime.datetime.now().year

# now1 = JalaliDateTime(year, month, day, 0, 0, 0, 0, pytz.utc).strftime("%B")
now2 = JalaliDateTime(year, month, day, 0, 0, 0, 0, pytz.utc).strftime("%A")
# print(now1)
print(now2)
