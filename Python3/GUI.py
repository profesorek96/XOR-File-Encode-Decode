import tkinter as tk
import main_logic
from tkinter import filedialog as fd

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x100")
        self.window.title("Xor File")
        self.path_in=""
        self.path_out=""
        self.key=int()

        selectF = tk.Button(self.window, text="Selec File to read", width=20, command=lambda :self.open_file())
        selectO = tk.Button(self.window, text="Selec File to write", width=20, command=lambda :self.save_file())
        self.name = tk.Entry(self.window, width=40)
        run = tk.Button(self.window, text="Run endcose/decode XOR", width=20, command=lambda :self.run_xor())
        selectF.pack()
        selectO.pack()
        self.name.pack()
        run.pack()

        self.window.mainloop()

    def open_file(self):
        self.path_in = fd.askopenfilename(filetypes=[("File", "*")])  # wywołanie okna dialogowego open file
        print(self.path_in)


    def save_file(self):
        self.path_out = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*")],defaultextension="*.txt")  # wywołanie okna dialogowego save file
        print(self.path_out)

    def run_xor(self):
        try:
            self.key = int(self.name.get())
            main_logic.main_Logic(self.path_in, self.path_out, self.key)
        except:
            print("Zdupilo sie")

apl = Application()