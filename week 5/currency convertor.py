import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")
        self.master.geometry("400x200")
        

        self.c = CurrencyRates()
        self.currencies = self.c.get_rates('USD')

        # Set font style
        self.font_style = ("Arial", 10)

        self.from_currency_var = tk.StringVar(master)
        self.to_currency_var = tk.StringVar(master)
        self.amount_var = tk.DoubleVar(master)
        self.result_var = tk.StringVar(master)

        # Labels
        from_currency_label = tk.Label(master, text="From Currency:", font=self.font_style, bg="#f0f0f0")
        from_currency_label.grid(row=0, column=0, padx=5, pady=5)
        to_currency_label = tk.Label(master, text="To Currency:", font=self.font_style, bg="#f0f0f0")
        to_currency_label.grid(row=1, column=0, padx=5, pady=5)
        amount_label = tk.Label(master, text="Amount:", font=self.font_style, bg="#f0f0f0")
        amount_label.grid(row=2, column=0, padx=5, pady=5)
        result_label = tk.Label(master, text="Result:", font=self.font_style, bg="#f0f0f0")
        result_label.grid(row=4, column=0, padx=5, pady=5)

        # Entry widgets
        self.from_currency_menu = tk.OptionMenu(master, self.from_currency_var, *self.currencies.keys())
        self.from_currency_menu.config(width=15, font=self.font_style)
        self.from_currency_menu.grid(row=0, column=1, padx=5, pady=5)
        self.to_currency_menu = tk.OptionMenu(master, self.to_currency_var, *self.currencies.keys())
        self.to_currency_menu.config(width=15, font=self.font_style)
        self.to_currency_menu.grid(row=1, column=1, padx=5, pady=5)
        self.amount_entry = tk.Entry(master, textvariable=self.amount_var, font=self.font_style, width=17)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        # Convert button
        convert_button = tk.Button(master, text="Convert", command=self.convert, font=self.font_style)
        convert_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(master, textvariable=self.result_var, font=self.font_style, bg="#f0f0f0")
        self.result_label.grid(row=4, column=1, padx=5, pady=5)

    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = self.amount_var.get()

        result = self.c.convert(from_currency, to_currency, amount)
        self.result_var.set(f"{result:.2f} {to_currency}")

def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
