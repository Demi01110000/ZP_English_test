# quiz_gui.py

from tkinter import Tk, Label, Radiobutton, Button

class QuizGUI:
    def __init__(self, matrix, logic):
        # Inicializace GUI pro kvíz
        self.matrix = matrix
        self.question_index = 0
        self.logic = logic

        self.window = Tk()
        self.window.title('Aplikace Kvízu')

        # Nastavení barvy pozadí na odstín růžové
        self.window.configure(bg='#FFD9EC')  

        # Nastavení popisku otázky s odstínem růžové
        self.question_label = Label(self.window, text="", font=("Verdana", 20), wraplength=500, bg='#FFD9EC')  # Nastavení barvy pozadí
        self.question_label.pack()

        # Inicializace tlačítek pro odpovědi s odstínem růžové
        self.options = []
        for i in range(1, len(self.matrix[0]) - 1):
            option = Radiobutton(self.window, text="", font=("Verdana", 15), value=i, command=lambda i=i: self.logic.check_answer(i), bg='#FFD9EC')  # Nastavení barvy pozadí
            option.pack()
            self.options.append(option)

        # Nastavení popisku skóre s odstínem odlišného růžového tónu
        self.score_label = Label(self.window, text="", font=("Verdana", 15), bg='#FFC3D4')  
        self.score_label.pack()

        # Tlačítko pro přechod na další otázku s odstínem odlišného růžového tónu
        next_button = Button




