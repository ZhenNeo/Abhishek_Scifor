import tkinter as tk 
from tkinter import scrolledtext
from tkinter import Menu, filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, text)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension= '.txt')
    if file_path:
        with open(file_path, 'w') as file:
            text = text_area.get(1.0, tk.END)
            file.write(text)

def about():
    messagebox.showinfo("About", "This is a simple notepad application built using tkinter")

root = tk.Tk()
root.title("Notepad")

text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.pack(expand=True, fill='both')

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=about)
menu_bar.add_cascade(label='Help', menu=help_menu)

root.config(menu=menu_bar)

root.mainloop()

