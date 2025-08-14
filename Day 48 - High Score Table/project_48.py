while True:
  print("🌟HIGH SCORE TABLE🌟")
  print()
  initials = input("Input your initials > ")
  score = input("Input your score > ")
  print()
  f = open("highscore.txt", "a+")
  f.write(f"{initials} {score}\n")
  f.close()

  print("Added to high score table.")
  add = input("Add another? y/n > ")
  if add == "n":
    break