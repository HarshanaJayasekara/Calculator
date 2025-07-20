from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator2")
        master.geometry('357x420+0+0')  # Fits all buttons comfortably
        master.config(bg='gray')
        master.resizable(False, False)

        self.expression = StringVar()
        self.current_input = ''

        # Display area
        entry = Entry(master, width=17, bg='white', font=('Arial Bold', 28), textvariable=self.expression)
        entry.place(x=0, y=0)

        # Button builder
        def create_button(text, x, y, cmd=None):
            action = cmd if cmd else lambda: self.append_to_expression(text)
            Button(master, width=11, height=4, text=text, relief='flat', bg='white', command=action).place(x=x, y=y)

        # Button layout (organized by function and visual logic)
        buttons = [
            # Top row: clear, percent, parentheses, divide
            ('C', 0, 50, self.clear), ('%', 90, 50), ('(', 180, 50), ('/', 270, 50),
            
            # Row 2: digits 4-6 and minus
            ('4', 0, 125), ('5', 90, 125), ('6', 180, 125), ('-', 270, 125),
            
            # Row 3: digits 1-3 and plus
            ('1', 0, 200), ('2', 90, 200), ('3', 180, 200), ('+', 270, 200),
            
            # Row 4: close parenthesis, zero, dot, evaluate
            (')', 0, 275), ('0', 90, 275), ('.', 180, 275), ('=', 270, 275, self.evaluate),
            
            # Bottom row: digits 8, 7, operator *, digit 9 — reordered properly
            ('8', 0, 350), ('7', 90, 350), ('*', 180, 350), ('9', 270, 350)
        ]

        for btn in buttons:
            create_button(*btn)

    def append_to_expression(self, value):
        self.current_input += str(value)
        self.expression.set(self.current_input)

    def clear(self):
        self.current_input = ''
        self.expression.set('')

    def evaluate(self):
        try:
            result = str(eval(self.current_input))
            self.expression.set(result)
            self.current_input = result
        except Exception:
            self.expression.set("Error")
            self.current_input = ''

root = Tk()
Calculator(root)
root.mainloop()
