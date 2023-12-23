import tkinter as tk
from calculator_logic import add, sub, mul, div

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("calculator")
        self.result_var = tk.StringVar()
        self.create_widgets()
    
    def create_widgets(self):
        entry = tk.Entry(self.master, textvariable=self.result_var, justify="right", from=("Arial", 14))
        entry = grid(row=0, column=0, columspan=4, sticky="nsew")
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]