import datetime

print("Event Countdown Timer")
today = datetime.date.today()
year = input("Enter the year: ")
month = input("Enter the month: ")
day = input("Enter the day: ")
event = datetime.date(int(year), int(month), int(day))
days = event - today
days = days.days

if days < 0:
    print(f"The event has already passed {abs(days)} day(s) ago. 😭")
elif days > 0:
    print(f"The event is {days} day(s) to go. 😊")
else:
    print("The event is today! 🥳")