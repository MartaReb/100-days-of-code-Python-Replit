print("Exam Grade Calculator")
print()
test_name = input("Enter the name of the test: ")
max_score = int(input("Enter the maximum score: "))
score_received = int(input("Enter the score received: "))
print()
percentage = round((score_received / max_score * 100),2)

print("You got", percentage, "% in", test_name, "test.")
if percentage >= 90:
  print("You got A+. Cogratulations!")
elif percentage >= 80:
  print("You got A. Good job!")
elif percentage >= 70:
  print("You got B. Nice!")
elif percentage >= 60:
  print("You got C. You can do better!")
elif percentage >= 50:
  print("You got D. You need to study more!")
elif percentage <= 49:
  print("You got U. You need to study more!")
else: 
  print("Try again!")
