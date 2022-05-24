import random

from lib.player import Player
from lib.result import result
from lib.colors import cyan, reset

from utils.clear import clear
from utils.announce import announce_choices, announce_hands
from utils.watch_signal import watch_signal

from display.display_beginning import display_beginning
from display.display_ending import display_ending

watch_signal()

display_beginning()
try:
  user_name = input("To begin, please enter your name: ")
except EOFError:
  print("\n")
  display_ending()
  exit(1)

while True:
  try:

    announce_choices(user_name)
    
    user_choice = input(f"(Type r, p, or s): ")

    player1 = Player(user_name, user_choice)
    player2 = Player("Computer", random.choice([ "ROCK", "PAPER", "SCISSORS" ]))
    
    announce_hands(player1, player2)

    result(player1.hand, player2.hand)

    play_again = input("\nPlay again? (y/n): ")

    if play_again.lower() != "y":
      break
  
  except EOFError:
    print("\n")
    break

display_ending()

  