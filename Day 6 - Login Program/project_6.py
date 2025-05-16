print("Secure Login")
print("--"*7)
username = input("What's your username? ")
password = input("What's your password? ")

if username == "John" and password == "admin1":
  print("Hello John!")
elif username == "Janne" and password == "admin2":
  print("Welcome Janne!")
elif username == "David" and password == "admin3":
  print("Hi David!")
else:
  print("You don't have an account here...sorry!")