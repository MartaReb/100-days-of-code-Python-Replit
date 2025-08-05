import random, time, os

list_of_veggy = ["carrot", "potato", "tomato", "onion", "lettuce", "cucumber", "pepper", "broccoli", "spinach", "garlic", "cabbage", "zucchini", "cauliflower", "pea", "bean", "corn", "radish", "eggplant", "celery"]
word = random.choice(list_of_veggy)
chossen_letters = []
lives = 6

while True:
  time.sleep(2)
  os.system("clear")
  print("🥦 Veggy-Hangman 🥦")
  letter = input("Choose a letter: ").lower()
  
  if letter in chossen_letters:
    print("You've tried that before")
    print()
    continue
  else:
    chossen_letters.append(letter)
    
  all_letters = True
  if letter in word:
    print("Correct!")
    for i in word:
      if i in chossen_letters:
        print(i, end="")
      else:
        print("_", end="")
        all_letters = False
    print()
  else:
    print("Nope, not in there.")
    lives -= 1
    all_letters = False

  if all_letters:
    print(f"You won with {lives} live(s) left!")
    exit()
    
  if lives == 0:
    print(f"Game over! The answer was {word}")
    exit()
  else:
    print(f"{lives} lives left.")
    print()
    