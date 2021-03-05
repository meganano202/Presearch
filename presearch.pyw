import tkinter as tk
import sys
from tkinter import *
from tkinter import messagebox
from selenium import webdriver

iniciar_bot = False
e1 = ""
e2 = ""
e3 = ""
e4 = ""


def infoadicional():
    messagebox.showinfo("Creditos",
                        "ESTE PROGRAMA HA SIDO CREADO Y DESEÑADO POR EL YOUTUBER meganano202 CON AYUDA DE tecnobillo EN STACKOVERFLOW ")


def licencia():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://hastebin.com/zokohasova.pl")


def oneclick():
    global iniciar_bot, e1, e2, e3, e4
    iniciar_bot = True
    e1, e2, e3, e4 = e1.get(), e2.get(), e3.get(), e4.get()
    master.destroy()


def youtube():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.youtube.com/c/meganano202")


def twitter():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://twitter.com/meganano202")


def show_entry_fields():
    print("Email: %s\nPassword: %s\nRepeat: %s\nTime: %s" % (e1.get(), e2.get(), e3.get(), e4.get()))


master = Tk()

background_image = PhotoImage(file="tenor.gif")
background_label = tk.Label(master, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

tk.Label(master,
         text="Email", fg="red", bg="#050213", font="Helvetica 10 bold").place(x=0, y=5)
tk.Label(master,
         text="Password", fg="blue", bg="#050213", font="Helvetica 10 bold").place(x=0, y=30)
tk.Label(master,
         text="Repeat", fg="red", bg="#050213", font="Helvetica 10 bold").place(x=0, y=55)
tk.Label(master,
         text="Time", fg="blue", bg="#050213", font="Helvetica 10 bold").place(x=0, y=80)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e2.config(show="*")
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.place(x=70, y=5, width=240)
e2.place(x=70, y=30, width=110)
e3.place(x=70, y=55, width=60)
e4.place(x=70, y=80, width=60)

barraMenu = Menu(master)
master.config(menu=barraMenu, width=300, height=300)

Archivo = Menu(barraMenu, tearoff=0)
Archivo.add_command(label="Salir", command=master.quit)

Ayuda = Menu(barraMenu, tearoff=0)
Ayuda.add_command(label="Creditos", command=infoadicional)
Ayuda.add_command(label="Licencia", command=licencia)

barraMenu.add_cascade(label="Ayuda", menu=Ayuda)
barraMenu.add_cascade(label="Archivo", menu=Archivo)

Button = tk.Button()

tk.Button(master,
          text='Start',
          command=oneclick).place(x=100, y=110)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"YouTube_icon.png")

# Resizing image to fit on button
photoimage = photo.subsample(3, 3)

# here, image option is used to
# set image on button
# compound option is used to align
# image on LEFT side of button
Channel_button = tk.Button(master, image=photo, command=youtube, bg="#050213").place(x=150, y=110)

master.title("Presearch by meganano202")
master.iconbitmap("G_XURdf8.ico")
master.geometry("330x140")
master.resizable(0, 0)

master.mainloop()

if iniciar_bot == True:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://presearch.org/login")
    time.sleep(2)
    elem = driver.find_element_by_name("email")
    elem.send_keys(e1)
    time.sleep(4)
    password_elem = driver.find_element_by_name("password")
    password_elem.send_keys(e2)
    time.sleep(60)
    for i in range(int(e3)):
        search_elem = driver.find_element_by_id("search").send_keys("meganano202", Keys.ENTER)
        time.sleep(int(e4))
        driver.back()
