print("Are you a superfan of 'Friends' or a fake fan?")
print("Answer these questions to find out.")
print()
question1 = input("How many times did Ross get married? ")
if question1 == "3":
  print("Correct!")
  question2 = input("Who said it: 'Oh, I wish I could, but I don’t want to.' ")
  if question2 == "Phoebe":
    print("That's right!")
    question3 = input("How many seasons of Friends are there in total? ")
    if question3 == "10":
      print("You got it! You are a true Friends fan!")
    else:
      print("Wrong!")
  else:
    print("Try again!")
else:
  print("Wrong! You are fake fan!")