from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E !")
print()
print("Please choose your weapon: write R for rock, P for paper or S for scissors")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
print()

print(f"Player 1 chose {player1} and Player 2 chose {player2}.")
if player1 == player2:
  print("It's a tie!")
elif player1 == "R" and player2 == "P" or player1 == "P" and player2 == "S" or player1 == "S" and player2 == "R":
  print("Player 2 wins!")
elif player1 == "R" and player2 == "S" or player1 == "S" and player2 == "P" or player1 == "P" and player2 == "R":
  print("Player 1 wins!")
else:
  print("Invalid input. Please write R, P, or S")