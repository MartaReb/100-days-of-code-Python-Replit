import time, os, random

def add():
  f = open("my_ideas.txt", "a+")
  idea = input("What is your idea? > ")
  f.write(f"{idea}\n")
  f.close()
  print("Nice! Your idea has been stored.")

def show():
  f = open("my_ideas.txt", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  print(random.choice(ideas))      
  
while True:
  print("🌟Idea Storage🌟")
  menu = input("Add an idea, see a random idea or quite (a/r/q)?  > ")
  if menu == "a":
    add()
  elif menu == "r":
    show()
  elif menu == "q":
    break
  time.sleep(3)
  os.system("clear")