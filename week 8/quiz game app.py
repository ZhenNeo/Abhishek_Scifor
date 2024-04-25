import tkinter as tk
from tkinter import messagebox

class QuizGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Jupiter", "Mars", "Saturn", "Earth"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
                "correct_answer": "William Shakespeare"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.radio_var = tk.StringVar()  
        
        self.create_widgets()
        self.display_question()
    
    def create_widgets(self):
        self.question_label = tk.Label(self, text="", wraplength=380)
        self.question_label.pack(pady=10)
        
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self, text="", variable=self.radio_var, value="", command=lambda: self.select_option())
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)
        
        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)
    
    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        
        options = question_data["options"]
        for i in range(4):
            self.radio_buttons[i].config(text=options[i], value=options[i])
        
        self.radio_var.set("")  
    
    def select_option(self):
        selected_option = self.radio_var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if selected_option == correct_answer:
            self.score += 1
        
    
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
            self.destroy()

if __name__ == "__main__":
    app = QuizGame()
    app.mainloop()
