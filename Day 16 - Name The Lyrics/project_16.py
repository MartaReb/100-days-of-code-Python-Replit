print("Fill in the blank lyrics!")
print()
print("Never going to ______ you up")
print()

attempt = 0
while True:
  word = input("The missing word is: ")
  attempt +=1
  if word == "give":
    break
  else:
    print("Nope, try again.")
print(f"Well done! It only took you {attempt} attempt(s).")