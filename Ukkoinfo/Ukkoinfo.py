from install import * 
from main import * 
import webbrowser
from customtkinter import *
from tkinter import *
from Ukkoinfo import * 
import random
import time
app = CTk()
app.config(background="#313131")
app.iconbitmap("Ukkoinfo_logo.ico")
app.geometry("500x500")
app.resizable(False, False)
app.title("Ukkoinfo")
canva = Canvas(app, height=500, width=500, background="#313131", highlightthickness=0)
canva.pack()
def ukko_channelle():
    webbrowser.open("https://youtube.com/@ukko28-o7r")
def quitter():
    exit()
def article():
    canva.delete("all")
    with open("articles\\ukkocopain.txt", "r", encoding="utf-8") as f:
        article1 = f.read()
    canva.create_text(10, 175, text=article1, fill='white', font=(20))
    def homme():
        canva.delete("all")
        mon_image = PhotoImage(file='ukko.png')
        ukkoacceuil = canva.create_image(150, 0, anchor=NW, image=mon_image)
        btnukkophto = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Chîne YT de Ukko", command=ukko_channelle, hover_color="#730102")
        quitterlogiciel = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Quitter", command=quitter, hover_color="#730102")
        articleukko = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Les copain de Ukko", command=article, hover_color="#730102")
        btnukkophto.pack()
        articleukko.pack()
        quitterlogiciel.pack()
        canva.create_window(25, 10, window=quitterlogiciel)
        canva.create_window(245, 10, window=articleukko)
        canva.create_window(250, 250, window=btnukkophto)
        canva.create_window(150, 0, window=ukkoacceuil)
    home = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Acceuil", command=homme, hover_color="#730102")
    home.pack()
    canva.create_window(25, 10, window=home)




btnukkophto = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Chîne YT de Ukko", command=ukko_channelle, hover_color="#730102")
quitterlogiciel = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Quitter", command=quitter, hover_color="#730102")
articleukko = CTkButton(app, height=20, width=50, fg_color="#00007f", text="Les Copain de Ukko", command=article, hover_color="#730102")
btnukkophto.pack()
articleukko.pack()
quitterlogiciel.pack()
canva.create_window(25, 10, window=quitterlogiciel)
canva.create_window(245, 10, window=articleukko)
canva.create_window(250, 250, window=btnukkophto)
mon_image = PhotoImage(file='ukko.png')
canva.create_image(150, 0, anchor=NW, image=mon_image)
app.mainloop()