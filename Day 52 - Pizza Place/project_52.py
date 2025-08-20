import time, os
pizza = []

try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except FileNotFoundError:
  f = open("pizza.txt", "w")
  f.close()

def add():
  while True:
    name = input("What is your name? ")
    try:
      qty = int(input("How many pizzas do you want? "))
    except ValueError:
      print("Please enter a number")
      break
      
    cost = 0
    size = input("What size do you want(s, m, l)? > ").lower()
    if size == "s":
      cost = 5
    elif size == "m":
      cost = 7
    elif size == "l":
      cost = 10
    else:
      print("Please enter a valid size")
      break  
    
    total = cost * qty

    row = [name, qty, total, size]
    pizza.append(row)
    break
    
def view():
  for row in pizza:
    print(f"Name: {row[0]}\nSize: {row[3]}\nQuantity: {row[1]}\nTotal: {row[2]}$")
    print()

    
while True:
  print("🌟The Best Pizza🌟")
  menu = input("Choose:\n1: Add Pizza\n2: View Pizzas\n> ")
  time.sleep(1)
  os.system("cls")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    print("Please, choose a valid option!")
  time.sleep(3)
  os.system("cls")
  f = open("pizza.txt", "w")
  f.write(str(pizza))
  f.close()