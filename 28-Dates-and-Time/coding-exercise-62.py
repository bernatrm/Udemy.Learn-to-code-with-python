# Declare a titanic variable pointing to a date object representing April 14th, 1912
# Declare an independence_day variable pointing to a date object representing July 4th, 1776
# Declare an alarm_clock variable set to a time object representing 05:45:00AM
# Declare a one_second_away variable set to a time object representing 11:59:59PM
from datetime import date, time

titanic = date(1912, 4, 14) 
independence_day = date(1776, 7, 4)
alarm_clock = time(5, 45)
one_second_away = time(23, 59, 59)

print(titanic)
print(independence_day)
print(alarm_clock)
print(one_second_away)