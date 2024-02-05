from tkinter import Tk, Button
from quiz_logic import start_quiz

def main():
    window = Tk()
    window.title('Test Application')

    btn_load_csv = Button(window, text="Load CSV", command=start_quiz)
    btn_load_csv.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
