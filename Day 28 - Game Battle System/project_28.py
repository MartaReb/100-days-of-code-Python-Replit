import random, time, os

def character():
  name = input("Name your Legend: ")
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  print()
  return name, type

def roll_dice(sides):
  return random.randint(1,sides)

def health():
  health_stat = roll_dice(6) * roll_dice(12) / 2 + 10
  return health_stat

def strength():
  strength_stat = roll_dice(6) * roll_dice(8)/ 2 + 12
  return strength_stat 

print("⚔️ BATTLE TIME ⚔️")
print()
name1, type1 = character()
print(name1, type1)
health1 = health()
strength1 = strength()
print("Health:", health1)
print("Strength:", strength1)
print()
print("Who are they battling?")
print()
name2, type2 = character()
print(name2, type2)
health2 = health()
strength2 = strength()
print("Health:", health2 )
print("Strength:", strength2)
time.sleep(3)
os.system("cls")

print("⚔️ BATTLE TIME ⚔️")
print("The battle begins!")
print()
time.sleep(4)
round = 1

while True:
  char1_dice = roll_dice(6)
  char2_dice = roll_dice(6)
  difference = abs(strength1 - strength2) + 1
  if char1_dice > char2_dice:
    health2 -= difference
    if round == 1:
      print(name1, "wins the first blow.")
    else:
      print(name1, "wins round", round)
      print(name2, "takes a hit, with", difference, "damage.")
  elif char1_dice < char2_dice:
    health1 -= difference
    if round == 1:
      print(name2, "wins the first blow.")
    else:
      print(name2, "wins round", round)
      print(name1, "takes a hit, with", difference, "damage.")
  else:
    print("Their swords clash in a draw.")

  print()
  print(name1, type1)
  print("Health:", health1)
  print()
  print(name2, type2)
  print("Health", health2)
  print()

  if health1 <= 0:
    print("Oh no!", name1 ,"has died!")
    print(name2,"destroyed", name1, "in", round, "rounds!")
    exit()
  elif health2 <= 0:
    print("Oh no", name2 ,"has died!")
    print(name1,"destroyed", name2, "in", round, "rounds!")
    exit()
  else:
    print("And they're both standing for the next round!")
    
  round += 1
  time.sleep(5)
  os.system("cls")
  print("⚔️ BATTLE TIME ⚔️")
  print("The battle continues!") 
  print()
