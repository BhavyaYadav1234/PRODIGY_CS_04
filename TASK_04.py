def simulate_keystroke(key):
  """
  Simulates storing a key press in a list (for demonstration purposes only).

  Args:
      key: The key that was pressed (string).
  """
  # Simulate storing key press (replace with actual implementation)
  stored_keys.append(key)
  print(f"Key Pressed: {key}")

def main():
  """
  Simulates a loop that listens for key presses and stores them.
  """
  global stored_keys  # Declare stored_keys as global for modification
  stored_keys = []
  while True:
    # Simulate getting a key press (replace with actual implementation)
    key = input("Press a key (or 'q' to quit): ")
    if key == 'q':
      break
    simulate_keystroke(key)

  # Display stored keys upon exiting the loop
  print("Stored Key Presses:")
  for key in stored_keys:
    print(key, end=" ")

if __name__ == "__main__":
  main()
