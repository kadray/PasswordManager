from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import DataStore as ds

class New_window(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title = "Main Password"
        self.geometry("400x200")
        self.attributes('-topmost', True)
        self.protocol("WM_DELETE_WINDOW",  self.disable_button)

        self.master=master
        self.typed_password = ttk.StringVar(value="")

        self.create_label()
        self.create_entry_password(self.typed_password)
        self.create_submit_button()

    def create_entry_password(self, variable):
        entry = ttk.Entry(master=self, textvariable=variable, style="secondary.Tentry")
        entry.pack(padx=10, pady=10)
        return

    def create_label(self):
        if(not ds.check_file_existence("database.csv")):
            text = "Set main password"
        else:
            text = "Insert main password"
        label = ttk.Label(master=self, text=text, style="secondary.Tlabel")
        label.pack(padx=10, pady=10)
        return

    def create_submit_button(self):
        button = ttk.Button(master=self, text="Submit",style="secondary.Tbutton")
        if(not ds.check_file_existence("database.csv")):
            button.bind("<Button-1>", self.new_password)
        else:
            button.bind("<Button-1>",self.check_password)
        button.pack(padx=10, pady=10)

    def check_password(self,arg):
        database=ds.Database(self.typed_password.get())
        db_password=database.get_password()
        if (self.typed_password.get() == db_password):
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
        db=ds.Database(self.typed_password.get())
        print(self.typed_password.get())
        db.initialize_database()
        self.master.is_closed_window = False
        self.destroy()
        return

    def disable_button(self):
        self.destroy()
        self.master.master_window.destroy()
        self.master.is_closed_window = True
        return