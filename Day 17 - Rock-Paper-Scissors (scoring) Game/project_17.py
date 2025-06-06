from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E !")
print("Please choose your weapon: write R for Rock, P for Paper or S for Scissors")

player1_score = 0
player2_score = 0

while True:
  print()
  player1 = input("Player 1 > ")
  player2 = input("Player 2 > ")
  print()
  print(f"Player 1 chose {player1} and Player 2 chose {player2}.")

  if player1 == player2:
    print("It's a tie!")
  elif player1 == "R" and player2 == "P" or player1 == "P" and player2 == "S" or player1 == "S" and player2 == "R":
    print("Score for Player 2!")
    player2_score += 1
  elif player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
    print("Score for Player 1!")
    player1_score += 1
  else:
    print("Invalid input. Please write R, P, or S!")

  print(f"Player 1 has {player1_score} point(s) and Player 2 has {player2_score} point(s)")

  if player1_score == 3 or player2_score == 3:
    print("Thanks for playing!")
    exit()
  else:
    continue