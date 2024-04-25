import tkinter as tk

def log(func):
        def wrapper(*args, **kwargs):
            print(f"Calling function: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Tkinter App")
        self.geometry("400x300")

        self.label = tk.Label(self, text='Enter a number: ')
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.result_label = tk.Label(self, text='')
        self.result_label.pack()
        
        self.button = tk.Button(self, text='Calculate', command=self.calculate)
        self.button.pack(pady=10)

        self._number = None
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        if value is None or isinstance(value, (int, float)):
            self._number = value
        else:
            raise ValueError("Number must be an integer or float")
        
    def calculate(self):
        try:
            number = float(self.entry.get())
            self.number = number

            square = list(map(lambda x: x**2, [self.number]))[0]
            fibonacci_seq = list(self.fibonacci(int(self.number)))
            self.result_label.config(text=f"The suare of {self.number} is {square} \nFibonacci sequence: {fibonacci_seq}")

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

    @log
    def fibonacci(self, n):
        a, b = 0, 1
        for i in range(n):
            yield a
            a, b = b, a+b


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()