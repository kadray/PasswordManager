import ttkbootstrap as ttk

class ExerciseApp(ttk.Frame):
    def __init__(self, master_window):
        super().__init__(master_window, padding=(20,20))
        self.pack()

        self.input = ttk.StringVar(value="")

        self.label_create()
        self.entry_create()
        self.button_create()

    def label_create(self):
        label = ttk.Label(self, text="Hello World")
        label.pack(padx=5, pady=5)
        return

    def button_create(self):
        button = ttk.Button(self, text="Click")
        button.bind("<Button-1>" , self.button_function)
        button.pack(padx=5, pady=5)
        return

    def entry_create(self):
        entry = ttk.Entry(self, textvariable=self.input)
        entry.pack(padx=5, pady=5)
        return

    def button_function(self, args):
        print(self.input.get())
        return

if __name__ == "__main__":
    app = ttk.Window(title="Zadanie 1",themename="morph")
    app.geometry("400x400")
    ExerciseApp(app)
    app.mainloop()