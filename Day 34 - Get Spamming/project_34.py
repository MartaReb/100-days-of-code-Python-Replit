import os, time
listOfEmail = []

def pretty_print():
  os.system("clear") 
  print("List of Emails:") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index+1}: {listOfEmail[index]}") 
  time.sleep(1)

def spamming():
  for item in range(len(listOfEmail)):
    os.system("clear")
    print(f"Email {item+1}")
    print(f"""
    Dear {listOfEmail[item]}, 
    It has come to our attention that 
    you're missing out on the amazing Replit 100 days of code. 
    We insist you do it right away. 
    If you don't we will pass on your email address to every 
    spammer we've ever encountered and also sign you up 
    to the My Little Pony newsletter, because that's neat. 
    We might just do that anyway.
    
    Love and hugs,
    Ian Spammington III""")
    time.sleep(4)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    pretty_print() 
  elif menu == "4":
    spamming()
  time.sleep(1)
  os.system("clear")