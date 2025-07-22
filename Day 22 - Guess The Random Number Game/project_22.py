import random
print("Welcome to Guess the Number.")
print()

correct_number = random.randint(1, 100)
attempt = 0

while True:
  user_number = int(input("Choose a number between 0 and 100: "))
  if user_number < 0:
    print("This is not a permitted number! Now we'll never know what the answer is …")
    exit()
  elif user_number < correct_number:
    print("Too low. Try again!")
    attempt += 1
  elif user_number > correct_number:
    print("Too high. Try again!")
    attempt += 1
  elif user_number == correct_number:
    print("You guessed the correct number! You are a winner! 🥳")
    break
  else:
    print("That is not a number I recognize.")
print("It took you", attempt, "attempt(s) to get the correct answer.")