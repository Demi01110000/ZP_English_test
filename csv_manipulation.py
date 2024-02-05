import csv
from tkinter import filedialog

def load_csv():
    file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if file_path:
        return list(csv.reader(open(file_path, "r"), delimiter=","))
