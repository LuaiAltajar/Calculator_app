import tkinter as tk


class Calculator:
    def __init__(self):
        self.operation = ""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.display = tk.Entry(self.root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        tk.Button(self.root, text="1", font=("Arial", 20),
                  command=lambda: self.enter_number("1")).grid(row=3, column=0, sticky="ew")
        tk.Button(self.root, text="2", font=("Arial", 20),
                  command=lambda: self.enter_number("2")).grid(row=3, column=1, sticky="ew")
        tk.Button(self.root, text="3", font=("Arial", 20),
                  command=lambda: self.enter_number("3")).grid(row=3, column=2, sticky="ew")
        tk.Button(self.root, text="4", font=("Arial", 20),
                  command=lambda: self.enter_number("4")).grid(row=2, column=0, sticky="ew")
        tk.Button(self.root, text="5", font=("Arial", 20),
                  command=lambda: self.enter_number("5")).grid(row=2, column=1, sticky="ew")
        tk.Button(self.root, text="6", font=("Arial", 20),
                  command=lambda: self.enter_number("6")).grid(row=2, column=2, sticky="ew")
        tk.Button(self.root, text="7", font=("Arial", 20),
                  command=lambda: self.enter_number("7")).grid(row=1, column=0, sticky="ew")
        tk.Button(self.root, text="8", font=("Arial", 20),
                  command=lambda: self.enter_number("8")).grid(row=1, column=1, sticky="ew")
        tk.Button(self.root, text="9", font=("Arial", 20),
                  command=lambda: self.enter_number("9")).grid(row=1, column=2, sticky="ew")
        tk.Button(self.root, text="0", font=("Arial", 20),
                  command=lambda: self.enter_number("0")).grid(row=4, column=1, sticky="ew")
        tk.Button(self.root, text="/", font=("Arial", 20),
                  command=lambda: self.enter_operation("/")).grid(row=2, column=3, sticky="ew")
        tk.Button(self.root, text="*", font=("Arial", 20),
                  command=lambda: self.enter_operation("*")).grid(row=3, column=3, sticky="ew")
        tk.Button(self.root, text="+", font=("Arial", 20),
                  command=lambda: self.enter_operation("+")).grid(row=4, column=0, sticky="ew")
        tk.Button(self.root, text="-", font=("Arial", 20),
                  command=lambda: self.enter_operation("-")).grid(row=4, column=2, sticky="ew")
        tk.Button(self.root, text="=", font=("Arial", 20),
                  command=lambda: self.enter_operation("=")).grid(row=4, column=3, sticky="ew")
        tk.Button(self.root, text="C", font=("Arial", 20),
                  command=lambda: self.clear()).grid(row=1, column=3, sticky="ew")
        self.root.mainloop()

    def enter_number(self, number):
        self.display.insert(tk.END, number)

    def enter_operation(self, operator):
        if operator == "=":
            self.operation = str(eval(self.display.get()))
            self.display.delete(0, tk.END)
            self.display.insert(0, self.operation)
        else:
            self.operation = operator
            self.display.insert(tk.END, operator)

    def clear(self):
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    m = Calculator()
