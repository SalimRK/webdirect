import tkinter
from customtkinter import *

x = 800
y = 500
icon_path = "webdirectlogo.ico"

class redirect_sites(CTk):
    pass


def add_clicked():
    print("add button clicked")


if __name__ == '__main__':
    # root
    root = CTk()
    set_appearance_mode("system")
    root.iconbitmap(icon_path)
    root.title("webDirect")
    root.geometry(f"{x}x{y}")


    # Frames
    top_frame = CTkFrame(root, width=x, height=50, border_width=5)
    web_frame = CTkFrame(root, width=x, height=y - 70, border_width=5)

    # Button
    add_button = CTkButton(top_frame, text="ADD", command=add_clicked)

    # labels
    web_label = CTkLabel(top_frame, text="website")
    redirect_label = CTkLabel(top_frame, text="redirect website")

    # Grids
    # root
    top_frame.grid(row=0, column=0, pady=10)
    web_frame.grid(row=1, column=0)
    # top_frame
    # web_label.grid(row=0, column=0)
    # redirect_label.grid(row=0, column=1)
    # add_button.grid(row=0, column=2)
    # web_frame

    root.mainloop()
