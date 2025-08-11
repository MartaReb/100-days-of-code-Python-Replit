import random, time, os

def create_bingo_card():
  global bingo_card
  numbers = []
  while len(numbers) < 8:
    number = random.randint(1,90)
    if number not in numbers:
      numbers.append(number)
    else:
      continue
  numbers.sort()
  
  bingo_card = [ [numbers[0], numbers[1], numbers[2]],[numbers[3], "BINGO", numbers[4] ],[numbers [5], numbers[6], numbers[7]]]

def pretty_print():
  for row in bingo_card:
    for num in row:
      print(f"{num:<5}", end="| ")
    print("\n-------------------")

create_bingo_card()
exes = 0
while True:
  pretty_print()
  num = int(input("Next Number: "))
  for row in bingo_card:
    for item in range(len(row)):
      if row[item] == num:
        row[item] = "X"
        exes+=1

  time.sleep(1)
  os.system("clear")
  
  if exes == 8:
    print("Congratulations! You have won!")
    break