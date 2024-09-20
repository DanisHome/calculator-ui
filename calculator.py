import tkinter as tk

def calculate(event=None):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def add_to_expression(text):
    entry.insert(tk.END, text)

# function to clear
def clear():
    entry.delete(0, tk.END)

# gui
root = tk.Tk()
root.title("Calculator Exapmle | github.gg/DanisHome")

# input
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: add_to_expression(t) if t != '=' else calculate())
    button.grid(row=row, column=col)

# clear buttons
clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# =
equal_button = tk.Button(root, text='=', width=5, height=2, font=('Arial', 18), command=calculate)
equal_button.grid(row=5, column=2, columnspan=2)

# enter --> =
root.bind('<Return>', calculate)

root.mainloop()
