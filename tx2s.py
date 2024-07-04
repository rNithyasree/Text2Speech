import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from gtts import gTTS
import os

root = Tk()
root.title("Text2Speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

def speaknow():
    text = text_area.get(1.0, "end-1c")  # Get text from Text widget
    gender = gender_combobox.get()
    speed = speed_combobox.get()

    
    gender_code = 'gu-IN-Wavenet-C'
    

    if text.strip():
        if speed == 'Fast':
            tts = gTTS(text, tld='com', slow=False)# lang=language,
        else:
            tts = gTTS(text, tld='com', slow=True)  # Default to slow speed  lang=language,

        # Save the speech to an audio file
        tts.save("text2speech.mp3")
        os.system("start text2speech.mp3")  # Play the saved speech

# Function for the "Save" button (placeholder)
def Download():
    print("Download functionality placeholder")

# Icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=70)
Top_frame.place(x=0, y=0)
logo = PhotoImage(file="phone.png")
Label(Top_frame, image=logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="Text2Speech", font="arial 25 bold", bg="white", fg="black").place(x=60, y=15)

text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=120, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="#305065", fg="white").place(x=530, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="#305065", fg="white").place(x=710, y=160)

gender_combobox = Combobox(root, values=['Female'], font="arial 14", state='readonly', width=10)
gender_combobox.place(x=525, y=200)
gender_combobox.set('Female')

speed_combobox = Combobox(root, values=['Fast','Slow'], font="arial 14", state='readonly', width=10)
speed_combobox.place(x=700, y=200)
speed_combobox.set('Fast')

btnicon = PhotoImage(file="speak2.png")
btn = Button(root, text="SPEAK", compound=LEFT, image=btnicon, width=130, font="arial 14 bold", command=speaknow)
btn.place(x=520, y=280)

btnicon2 = PhotoImage(file="download.png")
dwld = Button(root, text="Save", compound=LEFT, image=btnicon2, width=130, font="arial 14 bold", command=Download)
dwld.place(x=730, y=280)

root.mainloop()
