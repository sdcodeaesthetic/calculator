from tkinter import *
expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def keyboard_input():
    global expression
    expression = equation.get()
    equation.set(expression)


def evaluate_expression():
    keyboard_input()
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""


def absolute_value():
    global expression
    keyboard_input()
    try:
        expression = int(expression)
    except ValueError:
        equation.set("Error")
        expression = ""
    else:
        total = expression * (-1)
        total = str(total)
        equation.set(total)
        expression = total


def square_num():
    global expression
    keyboard_input()
    try:
        expression = int(expression)
    except ValueError:
        equation.set("Error")
        expression = ""
    else:
        total = expression ** 2
        total = str(total)
        equation.set(total)
        expression = total


def backspace_entry():
    keyboard_input()
    global expression
    expression = expression[:-1]
    equation.set(expression)


def clear_entry():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    root = Tk()
    root.title("Simple Calculator")
    root.geometry("300x267")

    equation = StringVar()
    expression_field = Entry(root, textvariable = equation, relief = RIDGE, bd = 20, bg = "powder blue")
    expression_field.grid(columnspan = 4, ipadx = 70)

    button_clear = Button(root, text = 'Clear', width = 8, height = 2, command = clear_entry)
    button_clear.grid(row = 2, column = 0)

    button_percent = Button(root, text = '+\-', width = 8, height = 2, command = absolute_value)
    button_percent.grid(row = 2, column = 1)

    button_square = Button(root, text = 'x\u00b2', width = 8, height = 2, command = square_num)
    button_square.grid(row = 2, column = 2)

    button_backspace = Button(root, text = '\u232B', width = 8, height = 2, command = backspace_entry)
    button_backspace.grid(row = 2, column = 3)

    button1 = Button(root, text = '1', width = 8, height = 2, command = lambda: press(1))
    button1.grid(row = 3, column = 0)

    button2 = Button(root, text = '2', width = 8, height = 2, command = lambda: press(2))
    button2.grid(row = 3, column = 1)

    button3 = Button(root, text = '3', width = 8, height = 2, command = lambda: press(3))
    button3.grid(row = 3, column = 2)

    button4 = Button(root, text = '4', width = 8, height = 2, command = lambda: press(4))
    button4.grid(row = 4, column = 0)

    button5 = Button(root, text = '5', width = 8, height = 2, command = lambda: press(5))
    button5.grid(row = 4, column = 1)

    button6 = Button(root, text = '6', width = 8, height = 2, command = lambda: press(6))
    button6.grid(row = 4, column = 2)

    button7 = Button(root, text = '7', width = 8, height = 2, command = lambda: press(7))
    button7.grid(row = 5, column = 0)

    button8 = Button(root, text = '8', width = 8, height = 2, command = lambda: press(8))
    button8.grid(row = 5, column = 1)

    button9 = Button(root, text = '9', width = 8, height = 2, command = lambda: press(9))
    button9.grid(row = 5, column = 2)

    button_decimal = Button(root, text = '.', width = 8, height = 2, command = lambda: press("."))
    button_decimal.grid(row = 6, column = 0)

    button0 = Button(root, text = '0', width = 8, height = 2, command = lambda: press(0))
    button0.grid(row = 6, column = 1)

    button_equal = Button(root, text = '=', width = 8, height = 2, command = evaluate_expression)
    button_equal.grid(row = 6, column = 2)

    button_plus = Button(root, text = '+', width = 8, height = 2, command = lambda: press("+"))
    button_plus.grid(row = 3, column = 3)

    button_minus = Button(root, text = '-', width = 8, height = 2, command = lambda: press("-"))
    button_minus.grid(row = 4, column = 3)

    button_multiply = Button(root, text = '*', width = 8, height = 2, command = lambda: press("*"))
    button_multiply.grid(row = 5, column = 3)

    button_divide = Button(root, text = '/', width = 8, height = 2, command = lambda: press("/"))
    button_divide.grid(row = 6, column = 3)

    root.mainloop()
