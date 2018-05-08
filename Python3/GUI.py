import tkinter as tk
import main_logic
from tkinter import filedialog as fd
from tkinter import messagebox
class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x100")
        self.window.title("Xor File Encode/Decode")
        self.path_in=""
        self.path_out=""
        self.key=int()
        self.duration=0
        self.selectF = tk.Button(self.window, text="Selec File to read", width=20, command=lambda :self.open_file())
        self.selectO = tk.Button(self.window, text="Selec File to write", width=20, command=lambda :self.save_file())
        self.name = tk.Entry(self.window, width=24)
        self.run = tk.Button(self.window, text="Run encode/decode XOR", width=20, command=lambda :self.run_xor())
        self.selectF.pack()
        self.selectO.pack()
        self.name.pack()
        self.run.pack()

        self.window.mainloop()

    def open_file(self):
        self.path_in = fd.askopenfilename(filetypes=[("File", "*")])
        print(self.path_in)


    def save_file(self):
        self.path_out = fd.asksaveasfilename(filetypes=[("File", "*")],defaultextension="*")
        print(self.path_out)

    def run_xor(self):
        try:
            self.key = int(self.name.get())
            self.duration=main_logic.main_Logic(self.path_in, self.path_out, self.key)
            messagebox.showinfo("XOR successful","Operation XOR in this file is successful \n Time XOR in Dll: {0} \n Time XOR in Python: {1}".format(self.duration.endC-self.duration.startC,self.duration.endP-self.duration.startP))
        except:
            messagebox.showinfo("Error","ERROR")
            print("Zdupilo sie")

apl = Application()
