import sys
import getpass

#Ask player 1 to pick
player1_sel = getpass.getpass("Player 1 pick Rock, Paper or Scissors: ")

try:
    while (player1_sel != 'rock') and (player1_sel != 'paper') and (player1_sel != 'scissors'):
        player1_sel = getpass.getpass("Player 1 pick Rock, Paper or Scissors: ")
    else:
        print("\nPlayer 1 has made a selection\n")
except KeyboardInterrupt:
    print("\nGame was aborted by player. Exiting...")

#Ask player 2 to pick
player2_sel = getpass.getpass("Player 2 pick Rock, Paper or Scissors: ")

try:
    while (player2_sel != 'rock') and (player2_sel != 'paper') and (player2_sel != 'scissors'):
        player2_sel = getpass.getpass("Player 2 pick Rock, Paper or Scissors: ")
    else:
        print("\nPlayer 2 has made a selection\n")
except KeyboardInterrupt:
    print("\nGame was aborted by player. Exiting...")

#Print the result
if player1_sel == player2_sel:
    print("No winner, try again")
elif player1_sel == 'rock' and player2_sel == 'paper':
    print("Player 2 wins")
elif player1_sel == 'rock' and player2_sel == 'scissors':
    print("Player 1 wins")
elif player1_sel == 'paper' and player2_sel == 'rock':
    print("Player 1 wins")
elif player1_sel == 'paper' and player2_sel == 'scissors':
    print("Player 2 wins")
elif player1_sel == 'scissors' and player2_sel == 'rock':
    print("Player 2 wins")
elif player1_sel == 'scissors' and player2_sel == 'paper':
    print("Player 1 wins")
