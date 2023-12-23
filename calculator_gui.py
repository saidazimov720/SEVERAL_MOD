import tkinter as tk
from calculator_logic import add, sub, mul, div

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("calculator")
        self.result_var = tk.StringVar()
        self.create_widgets()
    
    def create_widgets(self):
        entry = tk.Entry(self.master, textvariable=self.result_var, justify="right", font=('Arial', 14))
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        
        row_val, col_val = 1, 0
        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 12),
            command=lambda btn=button: self.button_click(btn)).grid(row=row_val, column=col_val)

            
            col_val +=1
            if col_val >3:
                col_val = 0
                row_val +=1
    
    def button_click(self, button):
        current_text = self.result_var.get()
        
        if button == 'C':
            self.result_var.set('')
        elif button == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('error')
            else:
                self.result_var.set(current_text + button)