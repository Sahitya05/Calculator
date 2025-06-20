import tkinter as tk

# Main Calculator Class
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("330x430")
        self.root.config(bg="#f0f0f0")
        
        self.expression = ""
        
        # Entry Field
        self.input_text = tk.StringVar()
        self.input_frame = tk.Entry(self.root, font=("Arial", 20), textvariable=self.input_text, bd=10, relief=tk.RIDGE, justify='right')
        self.input_frame.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=15, padx=10, pady=20)
        
        # Buttons
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        for i in range(4):
            for j in range(4):
                self.create_button(buttons[i][j], i+1, j)

    def create_button(self, value, row, column):
        btn = tk.Button(self.root, text=value, width=6, height=2, font=("Arial", 16), bd=5,
                        command=lambda: self.on_click(value), bg="#ffffff", fg="#333333")
        btn.grid(row=row, column=column, padx=5, pady=5)

    def on_click(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result  # Keep the result for further use
            except:
                self.input_text.set("Error")
                self.expression = ""
        elif value == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(value)
            self.input_text.set(self.expression)

# Run the Calculator
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
