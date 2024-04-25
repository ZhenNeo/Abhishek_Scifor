import random

class QuizGame:
    def __init__(self, topic, questions, answers, difficulty):
        self.topic = topic
        self.questions = questions
        self.answers = answers
        self.difficulty = difficulty
        self.points = 0

    def display_question(self, question_number):
        print("Question", question_number + 1, ":", self.questions[question_number])
    
    def check_answer(self, question_number, user_answer):
        correct_answer = self.answers[question_number]
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.points += 10
        else:
            print("Incorrect. The correct answer is:", correct_answer)
        
    def play_quiz(self):
        print("Welcome to the", self.difficulty, self.topic, "Quiz!")
        for i in range(len(self.questions)):
            self.display_question(i)
            user_answer = input("Enter your answer: ")
            self.check_answer(i, user_answer)
        print("Quiz complete! You scored", self.points, "points.")


questions = ["What is the capital of France?", "Who wrote 'To Kill a Mockingbird'?", "What is the chemical symbol for water?"]
answers = ["Paris", "Harper Lee", "H2O"]
topic = "General Knowledge"
difficulty = "Easy"

quiz = QuizGame(topic, questions, answers, difficulty)
quiz.play_quiz()
