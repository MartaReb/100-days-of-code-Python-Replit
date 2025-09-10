import os, time

admin_login = os.environ["admin"]
admin_password = os.environ["password1"]
user_login = os.environ["user"]
user_password = os.environ["password2"]

while True:
  print("🌟Login System🌟")
  login = input("Username > ")
  password = input("Password > ")
  
  if login == admin_login and password == admin_password:
    os.system("clear")
    print("Hello Admin!")
    break
  elif login == user_login and password == user_password:
    os.system("clear")
    print("Hello Normie!")
    break
  else:
    print("You are not allowed to enter")
    time.sleep(2)
    os.system("clear")