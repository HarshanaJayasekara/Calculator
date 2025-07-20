import tkinter as tk

calculator = ""

def add_to_calculator(symbol):
    global calculator
    calculator += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculator)

def evaluate_calculator():
    global calculator
    try:
        result = str(eval(calculator))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        calculator = result
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculator
    calculator = ""
    text_result.delete(1.0, "end")

# Initialize window
root = tk.Tk()
root.geometry("290x320")
root.title("Calculator 03")
root.iconbitmap("assets/pythontutorial.ico")

# Display field
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=4)

# Number buttons
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculator(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=0)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculator(1), width=5, font=("Arial", 14))
btn_1.grid(row=4, column=0)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculator(2), width=5, font=("Arial", 14))
btn_2.grid(row=4, column=1)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculator(3), width=5, font=("Arial", 14))
btn_3.grid(row=4, column=2)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculator(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculator(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculator(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=2)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculator(7), width=5, font=("Arial", 14))
btn_7.grid(row=2, column=0)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculator(8), width=5, font=("Arial", 14))
btn_8.grid(row=2, column=1)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculator(9), width=5, font=("Arial", 14))
btn_9.grid(row=2, column=2)

# Operators and functions
btn_add = tk.Button(root, text="+", command=lambda: add_to_calculator("+"), width=5, font=("Arial", 14))
btn_add.grid(row=2, column=3)

btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculator("-"), width=5, font=("Arial", 14))
btn_subtract.grid(row=3, column=3)

btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculator("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=3)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculator("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=3)

btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculator("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=5, column=1)

btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=5, column=2)

btn_equals = tk.Button(root, text="=",bg="orange", command=evaluate_calculator, width=25, font=("Arial", 14))
btn_equals.grid(row=6, column=0, columnspan=4)

# Parentheses
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculator("("), width=10, font=("Arial", 14))
btn_open.grid(row=1, column=0,columnspan=2)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculator(")"), width=10, font=("Arial", 14))
btn_close.grid(row=1, column=2, columnspan=2)

root.mainloop()
