"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import time
import datetime

startTime = time.perf_counter()

startDate = datetime.date(1901,1,1)
day = datetime.timedelta(1)
endDate = datetime.date(2000,12,31)

countSundays = 0
while (startDate != endDate):
    if (startDate.isoweekday() == 7 and startDate.day == 1):
        countSundays += 1
    startDate += day

print(countSundays)


endTime = time.perf_counter()
print("Time elapsed:", '{:0.6f}'.format(endTime - startTime), "seconds.")
