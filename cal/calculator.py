import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variables
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.operator = ""
        self.result = False
        
        # Create display frame
        self.display_frame = tk.Frame(self.root, bg='#2c3e50', height=100)
        self.display_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Display
        self.display = tk.Label(
            self.display_frame,
            text=self.current,
            font=('Arial', 24, 'bold'),
            bg='#2c3e50',
            fg='white',
            anchor='e',
            padx=20
        )
        self.display.pack(fill=tk.BOTH, expand=True)
        
        # Create button frame
        self.button_frame = tk.Frame(self.root, bg='#34495e')
        self.button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button configuration
        self.button_config = {
            'font': ('Arial', 16, 'bold'),
            'width': 4,
            'height': 2,
            'relief': 'raised',
            'bd': 2
        }
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        # Button layout
        buttons = [
            ['C', 'CE', '⌫', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '='],
            ['√', 'x²', '1/x', '%']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = tk.Button(
                    self.button_frame,
                    text=text,
                    command=lambda t=text: self.button_click(t),
                    **self.button_config
                )
                btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
                
                # Color coding (updated colors)
                if text in ['C', 'CE', '⌫']:
                    btn.config(bg='#c0392b', fg='white')  # darker red
                elif text in ['÷', '×', '-', '+', '=']:
                    btn.config(bg='#1abc9c', fg='white')  # teal
                elif text in ['√', 'x²', '1/x', '%', '±']:
                    btn.config(bg='#f1c40f', fg='black')  # yellow
                else:
                    btn.config(bg='#bdc3c7', fg='black')  # light gray
        
        # Configure grid weights
        for i in range(6):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, char):
        if char.isdigit():
            self.number_input(char)
        elif char == '.':
            self.decimal_input()
        elif char in ['÷', '×', '-', '+']:
            self.operator_input(char)
        elif char == '=':
            self.calculate()
        elif char == 'C':
            self.clear_all()
        elif char == 'CE':
            self.clear_entry()
        elif char == '⌫':
            self.backspace()
        elif char == '±':
            self.toggle_sign()
        elif char == '√':
            self.square_root()
        elif char == 'x²':
            self.square()
        elif char == '1/x':
            self.reciprocal()
        elif char == '%':
            self.percentage()
    
    def number_input(self, num):
        if self.result:
            self.current = "0"
            self.result = False
        
        if self.current == "0":
            self.current = num
        else:
            self.current += num
        
        self.update_display()
    
    def decimal_input(self):
        if self.result:
            self.current = "0"
            self.result = False
        
        if '.' not in self.current:
            self.current += '.'
            self.update_display()
    
    def operator_input(self, op):
        if self.operator and not self.result:
            self.calculate()
        
        self.total = float(self.current)
        self.operator = op
        self.input_value = True
        self.result = False
    
    def calculate(self):
        if self.operator and not self.result:
            try:
                if self.operator == '+':
                    self.total += float(self.current)
                elif self.operator == '-':
                    self.total -= float(self.current)
                elif self.operator == '×':
                    self.total *= float(self.current)
                elif self.operator == '÷':
                    if float(self.current) != 0:
                        self.total /= float(self.current)
                    else:
                        self.current = "Error: Division by zero"
                        self.update_display()
                        return
                
                self.current = str(self.total)
                if self.current.endswith('.0'):
                    self.current = self.current[:-2]
                
                self.operator = ""
                self.input_value = True
                self.result = True
                self.update_display()
            except:
                self.current = "Error"
                self.update_display()
    
    def clear_all(self):
        self.current = "0"
        self.total = 0
        self.operator = ""
        self.input_value = True
        self.result = False
        self.update_display()
    
    def clear_entry(self):
        self.current = "0"
        self.update_display()
    
    def backspace(self):
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
        self.update_display()
    
    def toggle_sign(self):
        if self.current != "0":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display()
    
    def square_root(self):
        try:
            num = float(self.current)
            if num >= 0:
                self.current = str(math.sqrt(num))
                if self.current.endswith('.0'):
                    self.current = self.current[:-2]
                self.result = True
                self.update_display()
            else:
                self.current = "Error: Invalid input"
                self.update_display()
        except:
            self.current = "Error"
            self.update_display()
    
    def square(self):
        try:
            num = float(self.current)
            self.current = str(num ** 2)
            if self.current.endswith('.0'):
                self.current = self.current[:-2]
            self.result = True
            self.update_display()
        except:
            self.current = "Error"
            self.update_display()
    
    def reciprocal(self):
        try:
            num = float(self.current)
            if num != 0:
                self.current = str(1 / num)
                if self.current.endswith('.0'):
                    self.current = self.current[:-2]
                self.result = True
                self.update_display()
            else:
                self.current = "Error: Division by zero"
                self.update_display()
        except:
            self.current = "Error"
            self.update_display()
    
    def percentage(self):
        try:
            num = float(self.current)
            self.current = str(num / 100)
            if self.current.endswith('.0'):
                self.current = self.current[:-2]
            self.result = True
            self.update_display()
        except:
            self.current = "Error"
            self.update_display()
    
    def update_display(self):
        # Limit display length
        if len(self.current) > 15:
            self.current = self.current[:15]
        
        self.display.config(text=self.current)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
