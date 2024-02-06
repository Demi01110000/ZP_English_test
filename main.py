from tkinter import Tk, Button
from quiz_logic import QuizLogic

def main():
    window = Tk()
    window.title('Test Application')

    logic = QuizLogic()
    btn_load_csv = Button(window, text="Load CSV", command=logic.start_quiz)
    btn_load_csv.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
