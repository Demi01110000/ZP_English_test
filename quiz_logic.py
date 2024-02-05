from tkinter import Label, Radiobutton, Button
from csv_manipulation import load_csv

def start_quiz():
    matrix = load_csv()
    if matrix:
        quiz = QuizGUI(matrix)
        quiz.run_quiz()

def check_answer(selected_option):
    # Add your answer checking logic here
    print(f"Selected option: {selected_option}")

def next_question():
    # Add logic for moving to the next question
    pass

class QuizGUI:
    def __init__(self, matrix):
        self.matrix = matrix
        self.question_index = 0

        self.window = None  # Initialize the Tkinter window here to avoid immediate creation
        self.options = []

    def run_quiz(self):
        self.window = Tk()
        self.window.title('Quiz Application')

        self.question_label = Label(self.window, text="", font=("Verdana", 20), wraplength=500)
        self.question_label.pack()

        for i in range(1, len(self.matrix[0])):
            option = Radiobutton(self.window, text="", font=("Verdana", 15), value=i, command=lambda i=i: check_answer(i))
            option.pack()
            self.options.append(option)

        next_button = Button(self.window, text="Next", command=self.next_question, font=("Verdana", 15))
        next_button.pack()

        self.update_display()
        self.window.mainloop()

    def update_display(self):
        # Update the display with the current question and options
        pass

    def show_final_score(self):
        # Add logic for displaying the final score
        pass

    def next_question(self):
        # Add logic for moving to the next question
        pass
