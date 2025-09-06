import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("200x200")

answer = 0
lastNumber = 0
operator = None

# Label to display current value or result
hello = tk.Label(text=answer)
hello.grid(row=0, column=1)

# Setting the current number (clicked by the user)
def user_number(value):
    global answer
    answer = int(value)
    hello["text"] = answer

# Storing the first number and the chosen operator
def action(op_action):
    global lastNumber, answer, operator
    lastNumber = answer
    operator = op_action
    hello["text"] = operator

# Performing the calculation based on the stored operator
def calc():
    global answer, lastNumber, operator
    if operator == "+":
        total = lastNumber + answer
    elif operator == "-":
        total = lastNumber - answer
    elif operator == "*":
        total = lastNumber * answer
    elif operator == "/":
        total = lastNumber / answer
    else:
        total = answer
    answer = total
    hello["text"] = answer


# Creating buttons for numbers and operators
one = tk.Button(text="1", command=lambda: user_number("1"))
one.grid(row=2, column=0)
two = tk.Button(text="2", command=lambda: user_number("2"))
two.grid(row=2, column=1)
three = tk.Button(text="3", command=lambda: user_number("3"))
three.grid(row=2, column=2)

add = tk.Button(text="+", command=lambda: action("+"))
add.grid(row=2, column=3)
minus = tk.Button(text="-", command=lambda: action("-"))
minus.grid(row=2, column=4)

four = tk.Button(text="4", command=lambda: user_number("4"))
four.grid(row=3, column=0)
five = tk.Button(text="5", command=lambda: user_number("5"))
five.grid(row=3, column=1)
six = tk.Button(text="6", command=lambda: user_number("6"))
six.grid(row=3, column=2)

multiply = tk.Button(text="*", command=lambda: action("*"))
multiply.grid(row=3, column=3)
divide = tk.Button(text="/", command=lambda: action("/"))
divide.grid(row=3, column=4)

seven = tk.Button(text="7", command=lambda: user_number("7"))
seven.grid(row=4, column=0)
eight = tk.Button(text="8", command=lambda: user_number("8"))
eight.grid(row=4, column=1)
nine = tk.Button(text="9", command=lambda: user_number("9"))
nine.grid(row=4, column=2)

zero = tk.Button(text="0", command=lambda: user_number("0"))
zero.grid(row=5, column=1)
equals = tk.Button(text="=", command=calc)
equals.grid(row=5, column=3)

window.mainloop()