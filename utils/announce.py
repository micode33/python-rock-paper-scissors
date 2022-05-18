from lib.colors import cyan, reset

def announce(message):
  print(f"{message}")

def announce_choices(user_name):
  print(f"Okay {user_name}, choose your hand... {cyan}ROCK, PAPER, SCISSORS{reset}?")

def announce_hands(user1, user2):
  print(f"\n{user1.name} chose {cyan + user1.hand.upper() + reset}, {user2.name} chose {cyan + user2.hand.upper() + reset}.\n")
  