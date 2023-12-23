import tkinter as tk
from calculator_logic import add, sub, mul, div

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("calculator")
        self.result_var = tk.StringVar()
        self.create_widgets()