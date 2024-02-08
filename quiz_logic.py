# quiz_logic.py

from tkinter import Tk
from quiz_gui import QuizGUI
from csv_manipulation import load_csv

class QuizLogic:
    def __init__(self):
        # Inicializace proměnných pro uchování dat
        self.matrix = []
        self.quiz_gui = None
        self.score = 0

    def start_quiz(self):
        # Načtení dat z CSV a zahájení kvízu
        self.matrix = load_csv()
        if self.matrix:
            self.quiz_gui = QuizGUI(self.matrix, self)
            self.quiz_gui.question_index = 1  # Začínáme od druhého řádku
            self.quiz_gui.run_quiz()

    def check_answer(self, selected_option):
        # Kontrola odpovědi a aktualizace skóre
        correct_option = int(self.matrix[self.quiz_gui.question_index][-1])
        print(f"Správná odpověď: {correct_option}, Vybraná odpověď: {selected_option}")

        if selected_option == correct_option:
            self.score += 1

    def next_question(self):
        # Přechod na další otázku nebo zobrazení finálního skóre
        self.quiz_gui.question_index += 1
        if self.quiz_gui.question_index < len(self.matrix):
            self.quiz_gui.load_question()
        else:
            self.quiz_gui.show_final_score()
