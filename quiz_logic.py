from tkinter import Label, Radiobutton, Button
from csv_manipulation import load_csv
from quiz_gui import QuizGUI

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
