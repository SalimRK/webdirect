import tkinter
from customtkinter import *
from PIL import Image, ImageTk

x = 800
y = 500
icon_path = "images/webdirectlogo.ico"
plusImg = CTkImage(Image.open(r"images/plusimage.png"))


class App(CTk):
    def __int__(self,selfFrame, site, redirect_website):
        super().__init__()
        self.selfFrame = CTkFrame(web_frame).grid(sticky="we")
        self.site = CTkEntry(selfFrame).grid(row=0, column=0, text="site")
        self.redirect_website = CTkEntry(selfFrame).grid(row=0, column=0,text="redirect website")


def add_clicked():
    query = Entry("f1")


if __name__ == '__main__':
    # root
    root = CTk()
    set_appearance_mode("system")
    root.iconbitmap(icon_path)
    root.title("webDirect")
    root.geometry(f"{x}x{y}")

    # Frames
    top_frame = CTkFrame(root, width=x, height=100)
    web_frame = CTkFrame(root, width=x, height=y - 70, border_width=5)

    # Button
    add_button = CTkButton(top_frame, text="ADD", image=plusImg, command=add_clicked)

    # labels
    web_label = CTkLabel(top_frame, text="website", padx=50)
    redirect_label = CTkLabel(top_frame, text="redirect website")

    # Grids
    # root
    top_frame.grid(row=0, column=0, pady=10, sticky="we")
    web_frame.grid(row=1, column=0)

    # top_frame
    web_label.grid(row=0, column=0)
    redirect_label.grid(row=0, column=1, padx=x / 4)
    add_button.grid(row=0, column=2)

    # web_frame

    root.mainloop()
