class Player:
  def __init__(self, name = "computer", selected = "r") -> None:
      
    self.name = name
    
    # Make selected all lowercase in case input is of different casing
    # and to ensure we make the correct selection
    selected = selected.lower()

    if selected == 'r' or selected == 'rock':
      self.hand = "rock"

    if selected == 'p' or selected == 'paper':
      self.hand = "paper"

    if selected == 's' or selected == 'scissors':
      self.hand = "scissors"

  def selected(self):
    print(self.hand)
