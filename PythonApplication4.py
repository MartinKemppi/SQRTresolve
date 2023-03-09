import tkinter as tk
from math import sqrt

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "No real roots"
    elif delta == 0:
        x = -b / (2*a)
        return f"Root: ({x})"
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return f"Roots: ({x1}, {x2})"

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    result_label.config(text=solve_quadratic(a, b, c))

root = tk.Tk()
root.title("Quadratic Equation Solver")

# Create labels and entries for coefficients
label_a = tk.Label(root, text="a:")
entry_a = tk.Entry(root)
label_b = tk.Label(root, text="b:")
entry_b = tk.Entry(root)
label_c = tk.Label(root, text="c:")
entry_c = tk.Entry(root)

# Create button to calculate the result
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Create label to display the result
result_label = tk.Label(root, text="Result: ")

# Place all the widgets using grid layout
label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_b.grid(row=1, column=0)
entry_b.grid(row=1, column=1)
label_c.grid(row=2, column=0)
entry_c.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
