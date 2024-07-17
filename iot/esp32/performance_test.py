'''
参考情報
CircuitPython: xshige's beta notes
https://beta-notes.way-nifty.com/blog/cat24261269/index.html

# Peformace Test for ESP32
'''
from machine import RTC


rtc = RTC()
rtc.datetime((2020, 2, 9, 1, 12, 48, 0, 0))
# (year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])


def performanceTest():
    secs = rtc.datetime()[6]
    endTime = secs + 10
    count = 0
    while rtc.datetime()[6] < endTime:
        count += 1
    print("Count: ", count)


print("Start Performance Test!")
performanceTest()
print("Finish Performance Test!")



