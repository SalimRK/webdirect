import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

x = 800
y = 500
icon_path = "images/webdirectlogo.ico"
plusImg = CTkImage(Image.open(r"images/plusimage.png"))


class EntryFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        site = CTkEntry(master=self)
        site.grid(row=0, column=0)

        redirect_website = CTkEntry(master=self)
        redirect_website.grid(row=0, column=1, padx=x / 4)

        deleteButton = CTkButton(master=self, text="delete", command=self.delete_clicked)
        deleteButton.grid(row=0, column=2)

    def delete_clicked(self):
        self.destroy()


class WebFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

    def add_clicked(self):
        entry = EntryFrame(self)
        entry.pack()


class TopFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        add_button = CTkButton(master=self, text="ADD", image=plusImg, command=self.add_clicked)
        web_label = CTkLabel(master=self, text="website", padx=50)
        redirect_label = CTkLabel(master=self, text="redirect website")

        web_label.grid(row=0, column=0)
        redirect_label.grid(row=0, column=1, padx=x / 4)
        add_button.grid(row=0, column=2)

    def add_clicked(self):
        self.master.web_frame.add_clicked()


class App(CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(icon_path)
        self.title("webDirect")
        self.geometry(f"{x}x{y}")

        self.top_frame = TopFrame(master=self)
        self.top_frame.grid(row=0, column=0, pady=10, sticky="we")
        self.web_frame = WebFrame(master=self, width=x, height=y - 70, border_width=5)
        self.web_frame.grid(row=1, column=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
