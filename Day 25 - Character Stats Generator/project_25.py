import random 

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("Character Stats Generator")
print()

while True:
  character = input("Name your warrior: ")
  health = roll_6_and_8()
  print(f"Their health is: {health}hp")
  makeCharacter = input("Want to create another character?yes/no ")
  if makeCharacter.lower() == "no":
    break