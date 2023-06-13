import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk

x = 800
y = 500

icon_path = "images/webdirectlogo.ico"
plusImg = CTkImage(Image.open(r"images/plusimage.png"))
closed_trash_image = CTkImage(Image.open(r"images/closed_trash_can.png"))
opened_trash_image = CTkImage(Image.open(r"images/open_trash_can.png"))


class EntryFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        # entry
        site = CTkEntry(master=self, state="disabled", width=200)

        redirect_website = CTkEntry(master=self, state="disabled", width=200)
        # switch
        self.switch_var = StringVar(value="off")
        self.switch = CTkSwitch(master=self, command=self.switch_event, variable=self.switch_var, onvalue="on",
                                offvalue="off")
        # deletbutton
        self.deleteButton = CTkButton(master=self, text="delete", command=self.delete_clicked,
                                      compound='left', image=closed_trash_image, fg_color="red")
        self.deleteButton.bind("<Enter>", self.on_enter)
        self.deleteButton.bind("<Leave>", self.on_leave)

        # grids
        site.grid(row=0, column=0, padx=10)
        redirect_website.grid(row=0, column=1, padx=30)
        self.switch.grid(row=0, column=2, padx=30)
        self.deleteButton.grid(row=0, column=3, padx=10)

    # switch methods
    def switch_event(self):
        print("switch toggled, current value:", self.switch_var.get())

    # delete button animation methods
    def on_enter(self, event):
        self.deleteButton.configure(image=opened_trash_image, fg_color="red")

    def on_leave(self, event):
        self.deleteButton.configure(image=closed_trash_image, fg_color="red")

    # delete button method
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
