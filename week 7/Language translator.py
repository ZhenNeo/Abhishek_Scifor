import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Translator")
        
        self.source_label = tk.Label(root, text="Enter text:")
        self.source_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.source_entry = tk.Entry(root)
        self.source_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.destination_label = tk.Label(root, text="Destination language:")
        self.destination_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.destination_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()))
        self.destination_combobox.grid(row=1, column=1, padx=10, pady=5)
        
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=5)
        
    def translate_text(self):
        translator = Translator()
        source_text = self.source_entry.get()
        destination_language = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.destination_combobox.get())]
        
        translated_text = translator.translate(source_text, dest=destination_language).text
        self.result_label.config(text=translated_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
