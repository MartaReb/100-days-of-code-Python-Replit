print("Which character from the 'Avengers' are you?")
print("Answer these questions and let's find out.")
print("Please use Y or N for yes or no.")
print("--"*20)
hanging_around = input("Do you like 'hanging around'?: ")
if hanging_around == "N":
  print("Then you're not Spider-man.")
else:
  print("You are Spider-man!")
gravelly = input("Do you have a 'gravelly' voice?: ")
if gravelly == "N":
  print("Aww, then you're not Korg.")
else:
  print("You are Korg!")
marvelous = input("Do you often feel 'Marvelous'?: ")
if marvelous =="Y":
  print("Aha! You're Captain Marvel! Hi!")
else:
  print("You're not Captain Marvel! :(")