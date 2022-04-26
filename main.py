from tkinter import *
from tkinter import messagebox
import requests


def tts(text):
    BASE_URL = "http://api.voicerss.org/"
    LANGUAGE = "en-in"
    SPEECH_VOICE = "Jai"

    params = {
        "key": "",
        "src": text,
        "hl": LANGUAGE,
        "v": SPEECH_VOICE
    }

    response = requests.request(
        "POST", BASE_URL, params=params)

    if response.status_code == 200:
        with open("audio.wav", "bx",) as f:
            f.write(response.content)


def convert():
    txt = txt_location_entry.get()

    if txt == "":
        messagebox.showinfo(title="Error", message="Insert file location")
    else:
        try:
            with open(f'{txt}', 'r') as file:
                data = file.read().replace('\n', ' ')
                print(f"Your text: {data}")
                tts(data)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File does not exist")
        finally:
            pass


window = Tk()
window.title("Text to speech app")
window.config(padx=50, pady=50)
window.geometry("600x550")

canvas = Canvas(height=180, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

txt_location = Label(text="Text location:").grid(row=1, column=0)

txt_location_entry = Entry(width=54)
txt_location_entry.grid(row=1, column=1)
txt_location_entry.focus()

add_button = Button(text="Convert into speech", width=46, command=convert).grid(row=3, column=1, columnspan=2)
quit_button = Button(text="Quit", command=window.destroy).grid(column=1, row=5)

window.mainloop()
