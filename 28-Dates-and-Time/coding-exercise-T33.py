from datetime import datetime

today = datetime(2000, 11, 17, 6, 0, 0)
print(today.strftime("%a"))
print(today.strftime("%B %d %Y"))
print(today.strftime("%j"))
print(today.strftime("%U"))
# "06:00:00 AM"
print(today.strftime("%I:%M:%S %p"))