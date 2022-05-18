import os

def clear():
  _ = 'clear' if os.name == 'posix' else 'cls'

  os.system(_)