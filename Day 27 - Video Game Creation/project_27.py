import random, time, os

def character():
  name = input("Name your Legend: ")
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return name, type

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def health():
  healthStat = rollDice(6) * rollDice(12) / 2 + 10
  return healthStat

def strength():
  strengthStat = rollDice(6) * rollDice(8)/ 2 + 12
  return strengthStat

while True:
  print("Character Builder")
  time.sleep(1)
  name, type = character()
  print(f"Name: {name}")
  print(f"Type: {type}")
  print("Health: ",health())
  print("Strength: ",strength())
  print("May your name go down in Legend...")
  print()
  again = input("Do you want to create another character (y/n)? ")
  print()
  if again == "n":
    time.sleep(1)
    os.system("cls")
    break
  else: 
    os.system("cls")
    continue