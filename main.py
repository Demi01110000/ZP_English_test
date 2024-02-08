# main.py

from tkinter import Tk, Button

from quiz_logic import QuizLogic

def main():
    # Vytvoření hlavního okna aplikace
    window = Tk()
    window.title('Testovací Aplikace')

    # Nastavení velikosti hlavního okna
    window.geometry("400x200")  # šířka a výška 

    # Nastavení barvy pozadí na odstín růžové
    window.configure(bg='#FFD9EC')  # kód barvy 

    # Inicializace instance třídy QuizLogic
    logic = QuizLogic()

    # Vytvoření tlačítka pro načtení CSV a spuštění kvízu
    btn_load_csv = Button(window, text="Načíst CSV a spustit kvíz", command=logic.start_quiz, bg='#FFD9EC')  # Nastavení barvy pozadí
    btn_load_csv.pack()

    # Spuštění hlavní smyčky aplikace
    window.mainloop()

if __name__ == "__main__":
    main()