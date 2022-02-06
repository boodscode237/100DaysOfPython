from datetime import date
from datetime import datetime
from datetime import timedelta

today = datetime.today()

print(type(today), today)

today_date = date.today()

print(type(today_date), today_date)

month_ = today_date.month

year_ = today_date.year

day_ = today_date.day

print(f"{day_}-{month_}-{year_}")

christmas = date(2022, 12, 25)

print((christmas - today_date).days)

if christmas is not today_date:
    print(f"Sorry there are still {christmas - today_date} days until christmas")
else:
    print("Yeah it's christmas")

t = timedelta(days=4, hours=10)

print(type(t))
print(t.days)
print(t.seconds)
print(t.seconds / 60 / 60)

eta = timedelta(days=100)
today = datetime.today()

print(eta + today)

print(str(today + eta))



