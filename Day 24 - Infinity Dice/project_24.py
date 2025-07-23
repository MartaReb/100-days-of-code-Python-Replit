import random 

def rollDice(sides):
  while True:
    number = random.randint(1, sides)
    print("You rolled", number)
    print()
    again = input("Roll again? ")
    if again == "yes":
      continue
    else:
      break

print("Infinity Dice 🎲")
print()
sides = int(input("Enter the number of sides: "))     
rollDice(sides)