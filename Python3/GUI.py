import tkinter as tk
import main_logic
from tkinter import filedialog as fd

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Xor File")

        self.menu = tk.Menu(self.window)

        submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Plik", menu=submenu)

        submenu.add_command(label="Otwórz", command=self.open_file)
        submenu.add_command(label="Zapisz", command=self.save_file)

        self.window.config(menu=self.menu, width=50, height=30)

        self.window.mainloop()

    def open_file(self):
        filename = fd.askopenfilename(filetypes=[("File", "*")])  # wywołanie okna dialogowego open file
        print(filename)
        try:
            main_logic.main_Logic(filename, "ola.txt", 5)
        except:
            print("Zdupilo sie")

    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*")],
                                        defaultextension="*.txt")  # wywołanie okna dialogowego save file

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))


apl = Application()

import tkinter as tk  # ładowanie modułu tkinter (w wersji 3+)

window = tk.Tk()  # tworzenie okna głównego
window.title("Hello World")  # ustawienie tytułu okna głównego
# tworzenie kontrolki typu label
text = tk.StringVar()
label = tk.Label(window, textvariable=text, padx=100, pady=20)
label.pack()  # podpinanie kontrolki pod okno
text.set(
    "Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności")
description = tk.Label(window, text="Podaj proszę swoje imie:").pack()
name = tk.Entry(window, width=40)
name.pack()


def HelloWorld():
    text.set(
        "Witaj {0} w świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności".format(
            name.get()))


ok = tk.Button(window, text="OK", width=20, command=HelloWorld)
ok.pack()

tk.mainloop()  # wywołanie pętli komunikatów