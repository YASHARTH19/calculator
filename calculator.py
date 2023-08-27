import tkinter as tk

def update_display(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + str(value))

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "ERROR")

def handle_button_click(button_label):
    if button_label == "=":
        calculate()
    elif button_label == "C":
        display.delete(0, tk.END)
    else:
        update_display(button_label)

root = tk.Tk()
root.title("CALCULATOR")

display = tk.Entry(root, font=('Arial', 20))
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
    '.'
]

row_num, col_num = 1, 0
for button_label in buttons:
    tk.Button(root, text=button_label, padx=20, pady=20, font=('Arial', 15), command=lambda label=button_label: handle_button_click(label)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()
