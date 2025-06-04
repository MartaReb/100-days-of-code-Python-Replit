print("Fill in the blank lyrics!")
print()
print("If you don't wanna see me dancing with somebody")
print("If you wanna believe that ... could stop me")
print()

attempt = 0
while True:
  word = input("The missing word is: ")
  attempt +=1
  if word == "anything":
    break
  else:
    print("Nope, try again.")
print("Well done! It only took you", attempt, "attempt(s).")