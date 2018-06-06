import time
import calendar

print(time.time())
print(time.localtime())
print(time.localtime(time.time())[0])
print(time.asctime(time.localtime(time.time())))
print(calendar.month(2018, 6))
print(time.altzone)
print(time.clock())
print(calendar.isleap(2016))
print(calendar.leapdays(2017, 2020))
time.sleep(3)
print(time.localtime(time.time())[5])
