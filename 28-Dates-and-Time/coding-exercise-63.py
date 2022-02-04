# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
# from datetime import date, time, datetime
# some_date = date(2002, 2, 22)
# some_time = time(9, 45, 23)
# one_from_two(some_date, some_time) => datetime object representing 2002-02-22 09:45:23

from datetime import date, time, datetime

def one_from_two(date, time):
    return datetime(date.year, date.month, date.day, time.hour, time.minute, time.second)

some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)
print(one_from_two(some_date, some_time)) # => datetime object representing 2002-02-22 09:45:23


