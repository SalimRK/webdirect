import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk
import re

x = 800
y = 500

hostFile = "hosts"
icon_path = "images/webdirectlogo.ico"
plusImg = CTkImage(Image.open(r"images/plusimage.png"))
closed_trash_image = CTkImage(Image.open(r"images/closed_trash_can.png"))
opened_trash_image = CTkImage(Image.open(r"images/open_trash_can.png"))
send_image = CTkImage(Image.open(r"images/sendimg.png"))
url_image = CTkImage(Image.open(r"images/URLimg.png"))
redirect_image = CTkImage(Image.open(r"images/redirectimg.png"))


def query(website, redirected):
    query_site = f"{website}         {redirected}"
    return query_site


def comment_query(file_name, query_text1, query_text2):
    query_text = query(query_text1, query_text2)
    with open(file_name, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip() == query_text:
            line = '# ' + line.lstrip()  # Add '#' at the start
        modified_lines.append(line)

    # Write modified lines back to the file
    with open(hostFile, 'w') as file:
        file.writelines(modified_lines)


def uncomment_query(file_name, query_text1, query_text2):
    query_text = query(query_text1, query_text2)
    with open(file_name, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip() == '# ' + query_text:
            line = line.lstrip('# ')  # Remove '#' at the start
        modified_lines.append(line)

    # Write modified lines back to the file
    with open(file_name, 'w') as file:
        file.writelines(modified_lines)


def delete_query(file_name, query_text1, query_text2):
    query_text = query(query_text1, query_text2)
    with open(file_name, 'r') as file:
        lines = file.readlines()
    modified_lines = []
    for line in lines:
        if line.strip() != query_text and line.strip() != '# ' + query_text:
            modified_lines.append(line)

    # Write modified lines back to the file
    with open(file_name, 'w') as file:
        file.writelines(modified_lines)


def load_query(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    pattern = r'^(?:# )?([^#].+?)\s{9}(\S+)$'
    matches = []

    for line in content:
        match = re.search(pattern, line)
        if match:
            g1 = match.group(1)
            g2 = match.group(2)
            matches.append((g1, g2))

    return matches


def get_query_state(file_name, query_text1, query_text2):
    pattern = query(query_text1, query_text2)
    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if line.strip() == pattern:
            return "on"
        elif line.strip() == f"# {pattern}":
            return "off"
    return "on"


class AddWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("350x300")
        self.title("Add Site")

        self.site = CTkEntry(master=self, width=200)
        self.redirect_website = CTkEntry(master=self, width=200)

        site_label = CTkLabel(master=self, text="IP/Website: ")
        site_label_img = CTkLabel(master=self, image=url_image, text="")
        redirect_site_label = CTkLabel(master=self, text="redirect to: ")
        redirect_site_label_img = CTkLabel(master=self, image=redirect_image, text="")

        self.addButton = CTkButton(master=self, command=self.add, text="", image=send_image, height=100)

        site_label_img.grid(row=0, column=0, padx=5, pady=20)
        site_label.grid(row=0, column=1, padx=5, pady=20)
        self.site.grid(row=0, column=2, padx=15, pady=20)
        redirect_site_label_img.grid(row=1, column=0, padx=5, pady=20)
        redirect_site_label.grid(row=1, column=1, padx=5, pady=20)
        self.redirect_website.grid(row=1, column=2, padx=15, pady=20)
        self.addButton.grid(row=2, column=0, columnspan=3, pady=20)

    def add(self):
        site_label_text = self.site.get()
        redirect_website_label_text = self.redirect_website.get()
        pattern = query(site_label_text, redirect_website_label_text)

        with open(hostFile, "r") as file:
            match_found = False
            for line in file:
                if re.search(pattern, line):
                    match_found = True

        if not match_found:
            with open(hostFile, "a") as file:
                file.write(pattern + "\n")
            self.master.master.web_frame.add_element(site_label_text, redirect_website_label_text, "on")
        else:
            print("already exist")
        self.destroy()


class EntryFrame(CTkFrame):
    def __init__(self, master, site_text, redirect_website_text, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.site_text = site_text
        self.redirect_website_text = redirect_website_text
        # entry
        self.site = CTkTextbox(master=self, width=200, height=30)
        self.site.insert("0.0", site_text)
        self.site.configure(state="disabled")
        self.redirect_website = CTkTextbox(master=self, width=200, height=30)
        self.redirect_website.insert("0.0", redirect_website_text)
        self.redirect_website.configure(state="disabled")

        # switch
        self.switch_var = StringVar(value="on")
        self.switch = CTkSwitch(master=self, command=self.switch_event, variable=self.switch_var, onvalue="on",
                                offvalue="off", fg_color="red")
        # delete button
        self.deleteButton = CTkButton(master=self, text="delete", command=self.delete_clicked,
                                      compound='left', image=closed_trash_image, fg_color="red")
        self.deleteButton.bind("<Enter>", self.on_enter)
        self.deleteButton.bind("<Leave>", self.on_leave)

        # grids
        self.site.grid(row=0, column=0, padx=10)
        self.redirect_website.grid(row=0, column=1, padx=30)
        self.switch.grid(row=0, column=2, padx=30)
        self.deleteButton.grid(row=0, column=3, padx=10)

    # switch methods
    def switch_event(self):
        if self.switch_var.get() == "off":
            self.switch.configure(fg_color="red")
            comment_query(hostFile, self.site_text, self.redirect_website_text)
        if self.switch_var.get() == "on":
            self.switch.configure(fg_color="red")
            uncomment_query(hostFile, self.site_text, self.redirect_website_text)

    # delete button animation methods
    def on_enter(self, event):
        self.deleteButton.configure(image=opened_trash_image, fg_color="red")

    def on_leave(self, event):
        self.deleteButton.configure(image=closed_trash_image, fg_color="red")

    # delete button method
    def delete_clicked(self):
        delete_query(hostFile, self.site_text, self.redirect_website_text)
        self.destroy()


class WebFrame(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        data = load_query(hostFile)
        for pair in data:
            site_text, redirect_website_text = pair
            switch = get_query_state(hostFile, site_text, redirect_website_text)
            self.add_element(site_text, redirect_website_text, switch)

    def add_element(self, site_text, redirect_website_text, switch_state):
        entry = EntryFrame(self, site_text, redirect_website_text)
        entry.switch_var.set(switch_state)
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
        if self.master.add_window is None or not self.master.add_window.winfo_exists():
            self.master.add_window = AddWindow(self)
        else:
            self.master.add_window.focus()


class App(CTk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(icon_path)
        self.title("webDirect")
        self.geometry(f"{x}x{y}")

        self.top_frame = TopFrame(master=self)
        self.top_frame.grid(row=0, column=0, pady=10, sticky="we")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.web_frame = WebFrame(master=self, width=x, height=y - 70, border_width=5)
        self.web_frame.grid(row=1, column=0)

        self.add_window = None


if __name__ == '__main__':
    app = App()
    app.mainloop()
