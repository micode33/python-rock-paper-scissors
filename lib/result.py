from lib.colors import *

def result(challengers_choice, opponents_choice):
  """ Determine the winner """

  if challengers_choice == opponents_choice:
      print(f"Both players selected {challengers_choice}. {cyan}It's a tie!{reset}")

  elif challengers_choice == "rock":

      if opponents_choice == "scissors":
          print(f"Rock smashes scissors! {green}You win!{reset}")
      else:
          print(f"Paper covers rock! {red}You lose{reset}")

  elif challengers_choice == "paper":

      if opponents_choice == "rock":
          print(f"Paper covers rock! {green}You win!{reset}")
      else:
          print(f"Scissors cuts paper! {red}You lose{reset}")

  elif challengers_choice == "scissors":
      if opponents_choice == "paper":
          print(f"Scissors cuts paper! {green}You win!{reset}")
      else:
          print(f"Rock smashes scissors! {red}You lose{reset}")