import tkinter as tk


class Calculator:
    def __init__(self):
        """
        Creates the root window, sets the title and dimensions and creates the display and buttons.
        """
        # Create the root window
        self.root = tk.Tk()

        # Set the window title
        self.root.title("Calculator")

        # Disable resizing of the window
        self.root.resizable(False, False)

        # Initialize an empty string to store the current operation
        self.operation = ""

        # Create the display area
        self.display = tk.Entry(self.root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # Create the buttons
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

        # Start the event loop
        self.root.mainloop()

    def enter_number(self, number):
        """
        Update the display with the entered number.
        :param: The number to be entered.
        :return: None
        """
        self.display.insert(tk.END, number)

    def enter_operation(self, operator):
        """
        Perform the specified operation and update the display.
        :param: The operation to be performed.
        :return: None
        """
        if operator == "=":
            # Evaluate the expression in the display
            self.operation = str(eval(self.display.get()))

            # Clear the display
            self.display.delete(0, tk.END)

            # Insert the result
            self.display.insert(0, self.operation)
        else:
            self.operation = operator
            # Update the display with the operator
            self.display.insert(tk.END, operator)

    def clear(self):
        # Clear the contents of the display.
        self.display.delete(0, tk.END)


if __name__ == "__main__":
    m = Calculator()
