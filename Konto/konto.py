import os
from tkinter import *
import random

root = Tk()
root.title("Mein Konto")
root.geometry("400x500")  # Einrichten des Fensters
root.resizable(0, 0)

data_path = "C:/Users/mofr6/OneDrive/Desktop/Konto/"
#iban = random.sample(range(10), 11)

class App:
    
    def __init__(self, window):
        self.label = Label(window, text="Deine IBAN:")
        self.label.place(x= 10, y=10)
        self.entry = Entry(window)
        self.entry.place(x=80, y=12)
        self.absenden_btn = Button(root, text="Absenden", command=self.check)
        self.absenden_btn.place(x=210, y=9)
        
    def check(self):
        iban = self.entry.get()
        if os.path.exists(data_path + str(iban) + ".txt"):
            print("True")
            self.setup()
        else:
            print("false")
            
    def setup(self, window):
        pass
    

app = App(root)

root.mainloop()