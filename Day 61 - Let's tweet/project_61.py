import datetime, os, time
from replit import db

def add_tweet():
  tweet = input("Enter your tweet: ")
  timestamp = datetime.datetime.now()
  timestamp = f"{timestamp}"
  db[timestamp] = tweet
  print(f"Tweet added: {tweet}")

def view_tweet():
  print("Displaying all tweets:")
  keys = list(db.keys())
  keys.sort(reverse=True)
  for key in keys:
    print(f"{db[key]}")

while True:
  print("Let's tweet!")
  menu = input("""
  1. Add a new tweet
  2. View all tweets
  > """)
  time.sleep(1)
  os.system("clear")
  
  if menu == "1":
    add_tweet()
  elif menu == "2":
    view_tweet()
  else:
    print("Invalid choice. Please try again.")
  time.sleep(3)
  os.system("clear")