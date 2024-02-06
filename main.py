# main.py
from tkinter import Tk, Button

from quiz_logic import QuizLogic

def main():
    window = Tk()
    window.title('Test Application')

    # Set the size of the main window
    window.geometry("400x200")  # Adjust the width and height as needed

    # Set background color to a shade of pink
    window.configure(bg='#FFD9EC')  # You can adjust the color code as needed

    logic = QuizLogic()
    btn_load_csv = Button(window, text="Load CSV and start the Quiz", command=logic.start_quiz, bg='#FFD9EC')  # Set background color
    btn_load_csv.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
