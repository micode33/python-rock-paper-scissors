import random
import signal

from lib.player import Player
from lib.result import result
from lib.colors import *

# Capture the signal interupt and close gracefully
def handler(signum, frame):
  print("\nClosing...")
  exit(1)

signal.signal(signal.SIGINT, handler)

# Get the user's name
user_name = input("Enter your name: ")

while True:

  possible_choices = [ "ROCK", "PAPER", "SCISSORS" ]

  user_choice = input("Enter a choice (rock, paper, scissors)[r, p, s]: ")

  player1 = Player(user_name, user_choice)
  player2 = Player("computer", random.choice(possible_choices))
  
  print(f"{player1.name} chose {cyan + player1.hand.upper() + reset}, {player2.name} chose {cyan + player2.hand.upper() + reset}.\n")

  result(player1.hand, player2.hand)

  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break
