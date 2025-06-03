exit = "no"

while exit != "yes":
  animal = input("What animal sound do you want to hear? ").lower()
  if animal == "cow":
    print("A cow goes moo.")
  elif animal == "dog":
    print("A dog goes woof.")
  elif animal == "cat":
    print("A cat goes meow.")
  elif animal == "sheep":
    print("A sheep goes baa.")
  elif animal == "pig":
    print("A pig goes oink.")
  elif animal == "horse":
    print("A horse goes neigh.")
  elif animal == "chicken":
    print("A chicken goes cluck.")
  else: 
    print("I don't know that animal sound. Try again.")
  
  exit = input("Do you want to exit? ").lower()