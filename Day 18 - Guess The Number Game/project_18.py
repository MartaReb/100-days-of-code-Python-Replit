print("Welcome to Guess The Number Game.")
print()
correct_number = 35
attempt = 1

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
  else:
    print("You guessed the correct number! You are a winner! 🥳")
    break

print(f"It took you {attempt} attempt(s) to get the correct answer.")