import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

x = 800
y = 500
icon_path = "images/webdirectlogo.ico"
plusImg = CTkImage(Image.open(r"images/plusimage.png"))


def add_clicked():
    print("clicked")


class WebFrame(CTkFrame):
    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class TopFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        add_button = CTkButton(master=self, text="ADD", image=plusImg, command=add_clicked)
        web_label = CTkLabel(master=self, text="website", padx=50)
        redirect_label = CTkLabel(master=self, text="redirect website")

        web_label.grid(row=0, column=0)
        redirect_label.grid(row=0, column=1, padx=x / 4)
        add_button.grid(row=0, column=2)


class App(CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(icon_path)
        self.title("webDirect")
        self.geometry(f"{x}x{y}")

        top_frame = TopFrame(master=self)
        top_frame.grid(row=0, column=0, pady=10, sticky="we")
        web_frame = WebFrame(master=self, width=x, height=y - 70, border_width=5)
        web_frame.grid(row=1, column=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
