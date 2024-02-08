# quiz_gui.py
from tkinter import Tk, Label, Radiobutton, Button

class QuizGUI:
    def __init__(self, matrix, logic):
        self.matrix = matrix
        self.question_index = 0
        self.logic = logic

        self.window = Tk()
        self.window.title('Aplikace na kvíz')  # Název okna

        # Nastavení pozadí na odstín růžové barvy
        self.window.configure(bg='#FFD9EC')  # Lze upravit kód barvy podle potřeby

        self.question_label = Label(self.window, text="", font=("Verdana", 20), wraplength=500, bg='#FFD9EC')  # Nastavení pozadí na odstín růžové barvy
        self.question_label.pack()

        self.options = []
        for i in range(1, len(self.matrix[0]) - 1):
            option = Radiobutton(self.window, text="", font=("Verdana", 15), value=i, command=lambda i=i: self.logic.check_answer(i), bg='#FFD9EC')  # Nastavení pozadí na odstín růžové barvy
            option.pack()
            self.options.append(option)

        # Nastavení pozadí na jiný odstín růžové barvy
        self.score_label = Label(self.window, text="", font=("Verdana", 15), bg='#FFC3D4')  # Lze upravit kód barvy podle potřeby
        self.score_label.pack()

        next_button = Button(self.window, text="Další", command=self.logic.next_question, font=("Verdana", 15), bg='#FFC3D4')  # Nastavení pozadí na jiný odstín růžové barvy
        next_button.pack()

    def run_quiz(self):
        self.load_question()
        self.window.mainloop()

    def load_question(self):
        question = self.matrix[self.question_index][0]
        options = self.matrix[self.question_index][1:-1]

        # Nastavení pozadí na odstín růžové barvy
        self.question_label.config(text=question, bg='#FFD9EC')

        for i, option in enumerate(options, start=1):
            self.options[i - 1].config(text=f"{chr(64 + i)}. {option}", bg='#FFD9EC')

    def show_final_score(self):
        # Nastavení pozadí na jiný odstín růžové barvy
        self.score_label.config(text=f"Váš skóre: {self.logic.score}", bg='#FFC3D4')
