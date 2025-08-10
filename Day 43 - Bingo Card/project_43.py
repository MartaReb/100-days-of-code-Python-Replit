import random

numbers = []
while len(numbers) < 8:
  number = random.randint(1,90)
  if number not in numbers:
    numbers.append(number)
  else:
    continue
numbers.sort()

bingo_card = [ [numbers[0], numbers[1], numbers[2]],
          [numbers[3], "BINGO", numbers[4] ],
          [numbers [5], numbers[6], numbers[7]]]

for row in bingo_card:
  for num in row:
    print(f"{num:<5}", end=" ")
  print("\n---------------")