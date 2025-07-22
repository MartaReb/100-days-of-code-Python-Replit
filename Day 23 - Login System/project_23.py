def login():
  while True:
    username = input("What is your username? ")
    password = input("What is your password? ")
    if username == "admin" and password == "1234":
      print("Welcome!")
      break
    else:
      print("I don't recognize that username or password. Try again!")
      continue
    
print("LOGIN SYSTEM")
login()