import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        
        self.height_label = tk.Label(root, text="Height (in cm):")
        self.height_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.weight_label = tk.Label(root, text="Weight (in kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)
    
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            
            bmi = weight / ((height / 100) ** 2)  # Convert height to meters
            
            result = f"Your BMI is: {bmi:.2f}\n"
            
            if bmi < 18.5:
                result += "Underweight"
                color = "red"
            elif bmi < 24.9:
                result += "Normal weight"
                color = "green"
            else :
                result += "Overweight"
                color = "red"
           
            
            self.result_label.config(text=result, fg=color)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for height and weight.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
