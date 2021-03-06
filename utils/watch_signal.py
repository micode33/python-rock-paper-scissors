import signal

# Capture the signal interupt and close gracefully
def signal_handler(signum, frame):
  print("\n")
  exit(1)

def watch_signal():
  signal.signal(signal.SIGINT, signal_handler)