import random, os

print("🌟Top Trumps🌟")
print()
print("Welcome to the Top Trumps 'Wild Animals'")
print()
animals = {}
animals["Lion"] =  {"Strength": 9, "Speed": 7, "Intelligence": 6,"Size": 8}
animals["Elephant"] = {"Strength": 10, "Speed": 3, "Intelligence": 9,"Size": 10}
animals["Cheetah"] = {"Strength": 5, "Speed": 10, "Intelligence": 6,"Size": 6}
animals["Gorilla"] = {"Strength": 8, "Speed": 5, "Intelligence": 7,"Size": 7}
animals["White Shark"] = {"Strength": 9, "Speed": 8, "Intelligence": 5,"Size": 9}
animals["Eagle"] = {"Strength": 6, "Speed": 9, "Intelligence": 8,"Size": 5}
animals["Tiger"] = {"Strength": 8, "Speed": 8, "Intelligence": 7,"Size": 7}
animals["Polar Bear"] = {"Strength": 9, "Speed": 6, "Intelligence": 6,"Size": 8}

while True:
  print("List of animals: ")
  for key in animals:
    print(key)
  print()
  user = input("Choose your card > ").title()
  comp = random.choice(list(animals.keys()))
  print("Computer has picked >", comp)
  print()
  answer = input("Choose your stat:\n1 for Strength, 2 for Speed, 3 for Intelligence or 4 for Size > ")
  if answer == "1":
    answer = "Strength"
  elif answer == "2":
    answer = "Speed"
  elif answer == "3":
    answer = "Intelligence"
  elif answer == "4":
    answer = "Size"
  print()
  print(f"{user}: {animals[user][answer]}")
  print(f"{comp}: {animals[comp][answer]}")
  print()
  if animals[user][answer] > animals[comp][answer]:
    print(user, "wins!")
  elif animals[user][answer] < animals[comp][answer]:
      print(comp, "wins!")
  else:
    print("Draw!")
  print()
  again = input("Again? y/n > ")
  if again == "n":
    break
  os.system("cls")