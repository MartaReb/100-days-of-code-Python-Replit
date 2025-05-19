print("Hello. Welcome to your daily affirmation generator.")
name = input("What is your name? ")
day = input("What day of the week is it? ")
print()
print(day + "'s affirmation for " + name + ":")
if day == "Monday" or day == "monday":
  print("I am in the right place at the right time, doing the right thing.")
elif day == "Tuesday" or day == "tuesday":
  print("Conscious breathing is my anchor.")
elif day == "Wednesday" or day == "wednesday":
  print("You are loved just for being who you are, just for existing, " + name)
elif day == "Thursday" or day == "thursday":
  print("The chance to love and be loved exists no matter where you are, " + name)
elif day == "Friday" or day == "friday":
  print("Am I good enough? Yes I am.")
elif day == "Saturday" or day == "saturday":
  print("The perfect moment is this one, " + name)
elif day == "Sunday" or day == "sunday":
  print("I am deliberate and afraid of nothing.")
else:
  print("There is no such day of the week so there is no affirmation. Try again.")
  