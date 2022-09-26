import os
from tkinter import *
from tkinter import simpledialog
import random

root = Tk()
root.title("Mein Konto")
root.geometry("400x500")  # Einrichten des Fensters
root.resizable(0, 0)

data_path = "C:/Users/Moritz Friedrich/Documents/Launcher/InformatikSchule/Konto/"

class App:
    
    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(window, width="400", height="500")
        self.label = Label(window, text="Deine Benutzer-ID:")
        self.label.place(x= 25, y=15)
        self.label2 = Label(window, text="Dein Passwort:")
        self.label2.place(x= 25, y=50)
        self.entry_p = Entry(window, show="*")
        self.entry_p.place(x=135, y=50)
        self.label1 = Label(root, text="Status:")
        self.label1.place(x= 110, y=80)
        self.entry = Entry(window)
        self.entry.place(x=135, y=17)
        self.absenden_btn = Button(window, text="Absenden", command=self.check)
        self.absenden_btn.place(x=275, y=25)
        self.canvas.create_line(0, 120, 400, 120, fill="black", width="1")
        self.canvas.create_line(0, 450, 50, 450, fill="black", width="1")
        self.canvas.create_line(140, 450, 400, 450, fill="black", width="1")
        self.label3 = Label(root, text="Einstellungen")
        self.label3.place(x=55, y=440)
        self.canvas.pack()
        
    def check(self):
        uid = self.entry.get()
        e_pw = self.entry_p.get()
        if os.path.exists(data_path + str(uid) + ".txt"):
            f = open(data_path + str(uid) + ".txt", "r")
            lines = f.readlines()
            self.pw = lines[2]
            if e_pw == self.pw:
                self.setup(root, str(uid))
                self.label1.config(text="Status: Anmeldung erfolgreich")
            else:
                self.label1.place(x=40, y=50)
                self.label1.config(text="Status: Falsches Passwort")
        else:
            self.label1.place(x=10, y=50)
            self.label1.config(text="Status: Kein zugehöriges Konto gefunden. Der Registrierungsprozess" + "\n" +
                               "beginnt." + 
                               "\n" + "Ihre eingegebene Benutzer-ID wird Ihrem Konto zugeordnet.")
            f = open(data_path + str(uid) + ".txt", "x")
            self.registration(root, str(uid))
            
    def registration(self, window, uid):
        self.uid = uid
        print("Registration hat erfolgreich begonnen.")
        self.label = Label(window, text="Dein Vorname:")
        self.label.place(x=25, y=150)
        self.label = Label(window, text="Dein Nachname:")
        self.label.place(x=25, y=190)
        self.label = Label(window, text="Dein Passwort:")
        self.label.place(x=25, y=230)
        self.entry_v = Entry(window)
        self.entry_v.place(x=135, y=150)
        self.entry_n = Entry(window)
        self.entry_n.place(x=135, y=190)
        self.entry_p = Entry(window, show="*")
        self.entry_p.place(x=135, y=230)
        self.confirm_btn = Button(window, text="Bestätigen", command=self.create_konto)
        self.confirm_btn.place(x=160, y=260)
        
    def create_konto(self):
        uid = self.entry.get()
        vorname = self.entry_v.get()
        nachname = self.entry_n.get()
        passwort = self.entry_p.get()
        self.uid = uid
        f = open(data_path + str(uid) + ".txt", "r+")
        lines = f.readlines()
        f.write(str(vorname) + " " + str(nachname) + "\n"
                "0\n" +
                str(passwort))
        self.label = Label(root, text="Ihr Konto wurde erstellt. Starten Sie die App neu.")
        self.label.place(x=70, y=230)
    
    def setup(self, window, uid):
        self.window = window
        f = open(data_path + uid + ".txt", "r+")
        lines = f.readlines()
        self.label = Label(window, text="Willkommen " + lines[0] + "", font="Arial")
        self.label.place(x= 10, y=130)
        self.kontostand = lines[1]
        if len(self.kontostand) == 5:
            self.kontostand = self.kontostand[0] + "," + self.kontostand[1] + self.kontostand[2] + self.kontostand[3] + self.kontostand[4]
            self.label = Label(window, text="Kontostand: " + self.kontostand + "€", font="Arial")
            self.label.place(x= 20, y=200)
        elif len(self.kontostand) == 6:
            self.kontostand = self.kontostand[0] + self.kontostand[1] + "," + self.kontostand[2] + self.kontostand[3] + self.kontostand[4] + self.kontostand[5]
            self.label = Label(window, text="Kontostand: " + self.kontostand + "€", font="Arial")
            self.label.place(x= 20, y=200)
        elif len(self.kontostand) == 7:
            self.kontostand = self.kontostand[0] + self.kontostand[1] + self.kontostand[2] + "," + self.kontostand[3] + self.kontostand[4] + self.kontostand[5] + self.kontostand[6]
            self.label = Label(window, text="Kontostand: " + self.kontostand + "€", font="Arial")
            self.label.place(x= 20, y=200)
        elif len(self.kontostand) == 8:
            self.kontostand = self.kontostand[0] + "," + self.kontostand[1] + self.kontostand[2] + self.kontostand[3] + "," + self.kontostand[4] + self.kontostand[5] + self.kontostand[6] + self.kontostand[7]
            self.label = Label(window, text="Kontostand: " + self.kontostand + "€", font="Arial")
            self.label.place(x= 20, y=200)
        else:
            self.kontostand = self.kontostand
            self.label = Label(window, text="Kontostand: " + self.kontostand + "€", font="Arial")
            self.label.place(x= 20, y=200)
        
        self.label = Label(window, text="Betrag:")
        self.label.place(x=50, y=350)
        self.label = Label(window, text="Empfänger-ID:")
        self.label.place(x=18, y=400)
        self.entry_e = Entry(window)
        self.entry_e.place(x=100, y=400)
        self.entry_b = Entry(window)
        self.entry_b.place(x=100, y=350)
        self.ueberweisen_btn = Button(window, text="Überweisung bestätigen", command=self.ueberweisen)
        self.ueberweisen_btn.place(x=250, y=360)
        
        self.passwort_btn = Button(window, text="Passwort ändern", command=self.passwort_change)
        self.passwort_btn.place(x=10, y=465)
        
    def ueberweisen(self):
        betrag = self.entry_b.get()
        empfaenger = self.entry_e.get()
        
    def passwort_change(self):
        uid = uid = self.entry.get()
        lines = []
        new_pw = simpledialog.askstring("Neues Passwort", "Wie soll dein neues Passwort lauten?", parent=root)
        with open(data_path + str(uid) + ".txt", "r") as f:
            lines = f.readlines()
        with open(data_path + str(uid) + ".txt", "w") as f:
            for number, line in enumerate(lines):
                if number not in [2]:
                    f.write(line)
                else:
                    f.write(new_pw)
app = App(root)

root.mainloop()
