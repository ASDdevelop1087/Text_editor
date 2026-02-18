import os
import keyboard
import string
import time
import threading

# This creates a tuple of 'abcdef...XYZ...0123...'
allowed_chars = tuple(string.ascii_letters + string.digits + string.punctuation + " ")

note1 = ""
note2 = ""

def display_text(txt):
    global final_note,note1,note2
    os.system('cls')
    note1 += txt
    print(note1 + "|" + note2)
    
def blink():
    while True:
        os.system('cls')
        print(note1 + "|" + note2)  
        time.sleep(0.5)  
        os.system('cls')
        print(note1 + " " + note2)
        time.sleep(0.5)

# 1. Create the thread
# timer_thread = threading.Thread(target=blink, daemon=False)

# # 2. Start the thread
# timer_thread.start()

while True:
    if len(note1 + "|" + note2)/10 == len(note1 + "|" + note2)//10 :
        note2 += "/n"
    while True:
        event = keyboard.read_event()


        if event.event_type == keyboard.KEY_DOWN:
            if event.name in allowed_chars:

                display_text(event.name)

            elif event.name == "space":

                display_text(" ")

            elif event.name == "backspace":

                note1 = note1[:-1]
                display_text("")

            elif event.name == "left":
                if note1 != "":

                    note2 = note1[-1] + note2
                    note1 = note1[:-1]
                    display_text("")

            elif event.name == "right":
                if note2 != "":

                    note1 += note2[0]
                    note2 = note2[1:]
                    display_text("")
                


            
            
            