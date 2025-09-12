from replit import db
import datetime, csv, os, time, random, hashlib

def hash_password(password, salt):
  return hashlib.sha256(f"{password}{salt}".encode()).hexdigest()

def add_entry():
  entry = input("Enter your diary entry: ")
  with open("diary.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([datetime.datetime.now(), entry])
    print("Entry added successfully")

def view_entries():
  try:
    with open("diary.csv") as file:
      reader = csv.reader(file)
      entries = list(reader)
      if not entries:
        print("No diary entries found.")
      else:
        for row in entries:
          print(f"{row[0]} - {row[1]}")
  except FileNotFoundError:
    print("No diary entries found.")

keys = db.keys()
if len(keys)<1:
  print("First Run > Create account")
  username1 = input("Username > ")
  password1 = input("Password > ")
  salt = random.randint(0,9999)
  password1 = hash_password(password1,salt)
  db[username1] = {"password": password1, "salt": salt}
else:
  print("Log in")
  username2 = input("Username > ")
  password2 = input("Password > ")
  if username2 not in keys:
    print("Username or password incorrect")
    exit()
  salt = db[username2]["salt"]
  password2 = hash_password(password2,salt)
  if db[username2]["password"] != password2:
    print("Username or password incorrect")
    exit()

while True:
  time.sleep(2)
  os.system("cls")
  print("""Welcome to your private diary
  1. Add a new entry
  2. View all entries
  3. Exit""")
  choice = input("> ")
  time.sleep(2)
  os.system("cls")
  if choice == "1":
    add_entry()
  elif choice == "2":
    view_entries()
  elif choice == "3":
    exit()
  else:
    print("Invalid choice")