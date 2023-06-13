import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

x = 800
y = 500
icon_path = "images/webdirectlogo.ico"
plusImg = CTkImage(Image.open(r"images/plusimage.png"))


# def add_clicked():
#     print("add clicked")


def delete_clicked():
    print("delete clicked")


class EntryFrame(CTkFrame):
    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        site = CTkEntry(master=self)
        site.grid(row=0, column=0, text="site")

        redirect_website = CTkEntry(master=self)
        redirect_website.grid(row=0, column=1, text="redirect website")

        deleteButton = CTkButton(master=self, text="delete", command=delete_clicked)
        deleteButton.grid(row=0, column=2)


class WebFrame(CTkFrame):
    def __int__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    @staticmethod
    def add_clicked(self):
        entry = EntryFrame()
        entry.grid(row=0, column=0)


class TopFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        add_button = CTkButton(master=self, text="ADD", image=plusImg, command=WebFrame.add_clicked)
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
