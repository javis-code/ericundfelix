from tkinter import Tk, Label, Button


class FirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is my first GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.yeet_button = Button(master, text="Yeeeeeeet", command=self.yeet)
        self.yeet_button.pack()

    def greet(self):
        print("Greetings!")

    def yeet(self):
        print("Yeet")


root = Tk()
my_gui = FirstGUI(root)
root.mainloop()
