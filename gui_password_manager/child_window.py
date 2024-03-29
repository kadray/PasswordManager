from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

class New_window(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title = "Main Password"
        self.geometry("400x200")
        self.protocol("WM_DELETE_WINDOW",  self.disable_button)

        self.master=master

        self.main_password = ttk.StringVar(value="haslo") #musi pobierac z bazy glowne haslo
        self.typed_password = ttk.StringVar(value="")

        self.create_label()
        self.create_entry_password(self.typed_password)
        self.create_submit_button()

    def create_entry_password(self, variable):
        entry = ttk.Entry(master=self, textvariable=variable, style="secondary.Tentry")
        entry.pack(padx=10, pady=10)
        return

    def create_label(self):
        if(self.main_password == ""):
            text = "Set main password"
        else:
            text = "Insert main password"
        label = ttk.Label(master=self, text=text, style="secondary.Tlabel")
        label.pack(padx=10, pady=10)
        return

    def create_submit_button(self):
        button = ttk.Button(master=self, text="Submit",style="secondary.Tbutton")
        if(self.main_password.get()==""):
            button.bind("<Button-1>", self.new_password)
        else:
            button.bind("<Button-1>",self.check_password)
        button.pack(padx=10, pady=10)

    def check_password(self,arg):
        if (self.typed_password.get() == self.main_password.get()):
            self.master.is_closed_window = False
            self.destroy()
        else:
            toast = ToastNotification(
                title="Wrong password!",
                message="Your password is wrong!",
                duration=2000
            )
            toast.show_toast()
        return

    def new_password(self,arg):
        self.main_password.set(value=self.typed_password.get()) #wpisanie do bazy danych musi być
        self.destroy()
        return

    def disable_button(self):
        self.destroy()
        self.master.master_window.destroy()
        self.master.is_closed_window = True
        return