from tkinter import Tk, Label, Radiobutton, Button

class QuizGUI:
    def __init__(self, matrix, logic):
        self.matrix = matrix
        self.question_index = 0
        self.logic = logic

        self.window = Tk()
        self.window.title('Quiz Application')

        self.question_label = Label(self.window, text="", font=("Verdana", 20), wraplength=500)
        self.question_label.pack()

        self.options = []
        for i in range(1, len(self.matrix[0]) - 1):  # Adjusted to exclude the last column (Correct Answer)
            option = Radiobutton(self.window, text="", font=("Verdana", 15), value=i, command=lambda i=i: self.logic.check_answer(i))
            option.pack()
            self.options.append(option)

        next_button = Button(self.window, text="Next", command=self.logic.next_question, font=("Verdana", 15))
        next_button.pack()

    def run_quiz(self):
        self.load_question()
        self.window.mainloop()

    def load_question(self):
        question = self.matrix[self.question_index][0]
        options = self.matrix[self.question_index][1:-1]  # Exclude the last column (Correct Answer)

        self.question_label.config(text=question)

        for i, option in enumerate(options, start=1):
            self.options[i - 1].config(text=f"{chr(64 + i)}. {option}")

    def show_final_score(self):
        # Add logic for displaying the final score
        pass
