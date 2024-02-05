from tkinter import Tk, Label, Radiobutton, Button
from quiz_logic import check_answer

class QuizGUI:
    def __init__(self, matrix):
        self.matrix = matrix
        self.question_index = 0

        self.window = Tk()
        self.window.title('Quiz Application')

        self.question_label = Label(self.window, text="", font=("Verdana", 20), wraplength=500)
        self.question_label.pack()

        self.options = []

        for i in range(1, len(matrix[0])):
            option = Radiobutton(self.window, text="", font=("Verdana", 15), value=i, command=lambda i=i: check_answer(i))
            option.pack()
            self.options.append(option)

        self.next_button = Button(self.window, text="Next", command=self.next_question, font=("Verdana", 15))
        self.next_button.pack()

    def run_quiz(self):
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
