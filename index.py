import tkinter as tk
from math import sqrt

SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGIT_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE ="#CCEDFF"

class PyCalcu:
    def __init__(self): 
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("PyCalcu")

        self.total_expression = ""
        self.current_expression = ""
        self.digits = {
            7:(1, 1), 8:(1, 2), 9:(1, 3),
            4:(2, 1), 5:(2, 2), 6:(2, 3),
            1:(3, 1), 2:(3, 2), 3:(3, 3),
            0:(4, 2), ".":(4, 1)
        }
        self.operations = {
            "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"
        }

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        self.total_label, self.label = self.create_display_label()

        self.button_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

        self.create_digits_button()
        self.create_operator_button()
        self.create_special_button()

    def create_special_button(self):
        self.create_clear_button()
        self.create_equal_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")
        
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")
        
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digits_button(self): 
        for digit, grid_value in self.digits.items():
            digit_button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            digit_button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_button(self): 
        i = 0
        for operator, symbol in self.operations.items():
            opt_button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            opt_button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
    
    def create_clear_button(self):
        clr_button = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: self.clear())
        clr_button.grid(row=0, column=1, sticky=tk.NSEW)
    
    def create_equal_button(self): 
        eql_button = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda: self.evaluate())
        eql_button.grid(row=4, column=3, columnspan=3, sticky=tk.NSEW)

    def create_square_button(self): 
        eql_button = tk.Button(self.button_frame, text="x\u00b2", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.square)
        eql_button.grid(row=0, column=2, sticky=tk.NSEW)
    
    def create_sqrt_button(self): 
        eql_button = tk.Button(self.button_frame, text="\u221ax", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
        eql_button.grid(row=0, column=3, sticky=tk.NSEW)
    
    def add_to_expression(self, value): 
        self.current_expression += str(value)
        self.update_label()
        
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def append_operator(self, operator): 
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()
    
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(round(eval(self.total_expression), 7))
        self.total_expression = ""
        self.update_label()
    
    def sqrt(self):
        self.current_expression = str(round(eval(f'{self.current_expression}**0.5'), 7))
        self.update_label()

    def square(self): 
        self.current_expression = str(round(eval(f'{self.current_expression}**2'), 7))
        self.update_label()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    pyCalcu = PyCalcu()
    pyCalcu.run()