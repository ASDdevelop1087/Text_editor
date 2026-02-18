import os
import keyboard
import string

# This creates a tuple of 'abcdef...XYZ...0123...'
allowed_chars = tuple(string.ascii_letters + string.digits + string.punctuation + " ")

def display_text(txt):
    global note
    os.system('cls')
    note += txt
    print(note)
note = ""
while True:

    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN:
        if event.name in allowed_chars:
            
            display_text(event.name)
        elif event.name == "space":
            display_text(" ")
        elif event.name == "backspace":
            note = note[:-1]
            display_text("")
            
            
            