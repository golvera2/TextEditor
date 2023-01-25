import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        self.text = tk.Text(master, wrap='word')
        self.text.pack()

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

    def open_file(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r') as f:
                text = f.read()
                self.text.insert('1.0', text)

    def save_file(self):
        filepath = filedialog.asksaveasfilename()
        if filepath:
            with open(filepath, 'w') as f:
                text = self.text.get("1.0", 'end-1c')
                f.write(text)


if __name__ == '__main__':
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
