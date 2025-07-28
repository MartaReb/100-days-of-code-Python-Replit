def newPrint(color,word):
  if color == "green":
    print("\033[0;32m", word, sep="", end="")
  elif color == "red":
    print("\033[0;31m", word, sep="", end="")
  elif color == "blue":
    print("\033[0;34m", word, sep="", end="")
  elif color == "yellow":
    print("\033[1;33m", word, sep="", end="")
  elif color == "reset":
    print("\033[0m", word, sep="", end="")
  
print("Super Function")
print("With my ", end="")
newPrint("green", "new program")
newPrint("reset", " I can just call red ('and') ")
newPrint("red", "it will print in red ")
newPrint("blue", "or even blue.")
print()
newPrint("reset", "With no ")
newPrint("yellow", "weird gaps.")