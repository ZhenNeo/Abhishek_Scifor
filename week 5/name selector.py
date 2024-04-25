import tkinter as tk
from tkinter import messagebox
import random

class RandomNamePicker:
    def __init__(self, root, student_list):
        self.root = root
        self.root.title("Random Name Picker")
        self.student_list = student_list
        self.completed_list = []

        self.name_frame = tk.Frame(root)
        self.name_frame.pack(pady=20)
        self.name_label = tk.Label(self.name_frame, text="")
        self.name_label.pack()

        self.pick_button = tk.Button(root, text="Pick a Random Name", command=self.pick_random_name)
        self.pick_button.pack(pady=10)

        self.complete_frame = tk.Frame(root)
        self.complete_frame.pack(pady=10)
        self.complete_label = tk.Label(self.complete_frame, text="Completed Names:")
        self.complete_label.pack(side=tk.LEFT)
        self.completed_names = tk.Label(self.complete_frame, text="")
        self.completed_names.pack(side=tk.LEFT)

    def pick_random_name(self):
        if self.student_list:
            random_name = random.choice(self.student_list)
            self.student_list.remove(random_name)
            self.completed_list.append(random_name)

            self.name_label.config(text=random_name)
            self.completed_names.config(text=", ".join(self.completed_list))
        else:
            messagebox.showinfo("Alert", "No more names to pick!")

if __name__ == "__main__":
    student_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

    root = tk.Tk()
    root.geometry("500x500")
    app = RandomNamePicker(root, student_list)
    root.mainloop()
