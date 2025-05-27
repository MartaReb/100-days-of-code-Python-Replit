days_this_year = int(input("How many days are in this year? "))
days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

result_365 = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

result_366 = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute

if days_this_year == 366:
  print("There are", result_366, "seconds in a leap year.")
elif days_this_year == 365:
  print("There are", result_365, "seconds in this year.")
else:
  print("Not possible! Check again!")