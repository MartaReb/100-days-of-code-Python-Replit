import dice_rolling as rol

print("Character Stats Generator")
print()

while True:
  character = input("Name your warrior: ")
  health = rol.roll_6_and_8()
  print(f"Their health is: {health}hp")
  makeCharacter = input("Want to create another character?yes/no ")
  if makeCharacter.lower() == "no":
    break