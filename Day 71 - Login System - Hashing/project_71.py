import time, os, random

users_list = {}

def add_user():
  username = input("Username > ")
  password = input("Password > ")
  if username in users_list:
    print("ERROR: Username exists")
    return
  salt = random.randint(1000, 9999)
  password = f"{password}{salt}"
  password = hash(password)
  users_list[username] = {"password": password, "salt": salt}
  print("User added")

def login():
  username = input("Username > ")
  password = input("Password > ")
  if username in users_list:
    salt = users_list[username]["salt"]
    password = f"{password}{salt}"
    password = hash(password)
    if users_list[username]["password"] == password:
      print("Login successful")
    else:
      print("Wrong password")
  else:
    print("Username not found")
    
while True:
  print("🌟Login System🌟")
  menu = input("1. Add User\n2. Login\n> ")
  time.sleep(1)
  os.system("cls")
  if menu == "1":
    add_user()
  elif menu == "2":
    login()
  else:
    print("Invalid option")
  time.sleep(2)
  os.system("cls")