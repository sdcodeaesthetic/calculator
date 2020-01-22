from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.geometry("300x225")

equation = StringVar()
expression_field = Entry(root, textvariable = equation, relief = RIDGE, bd = 20, bg = "powder blue")
expression_field.grid(columnspan = 4, ipadx = 70)

button1 = Button(root, text = '1', width = 8, height = 2)
button1.grid(row = 2, column = 0)

button2 = Button(root, text = '2', width = 8, height = 2)
button2.grid(row = 2, column = 1)

button3 = Button(root, text = '3', width = 8, height = 2)
button3.grid(row = 2, column = 2)

button4 = Button(root, text = '4', width = 8, height = 2)
button4.grid(row = 3, column = 0)

button5 = Button(root, text = '5', width = 8, height = 2)
button5.grid(row = 3, column = 1)

button6 = Button(root, text = '6', width = 8, height = 2)
button6.grid(row = 3, column = 2)

button7 = Button(root, text = '7', width = 8, height = 2)
button7.grid(row = 4, column = 0)

button8 = Button(root, text = '8', width = 8, height = 2)
button8.grid(row = 4, column = 1)

button9 = Button(root, text = '9', width = 8, height = 2)
button9.grid(row = 4, column = 2)

button_clear = Button(root, text = 'Clear', width = 8, height = 2)
button_clear.grid(row = 5, column = 0)

button0 = Button(root, text = '0', width = 8, height = 2)
button0.grid(row = 5, column = 1)

button_equal = Button(root, text = '=', width = 8, height = 2)
button_equal.grid(row = 5, column = 2)

button_plus = Button(root, text = '+', width = 8, height = 2)
button_plus.grid(row = 2, column = 3)

button_minus = Button(root, text = '-', width = 8, height = 2)
button_minus.grid(row = 3, column = 3)

button_multiply = Button(root, text = '*', width = 8, height = 2)
button_multiply.grid(row = 4, column = 3)

button_divide = Button(root, text = '/', width = 8, height = 2)
button_divide.grid(row = 5, column = 3)

root.mainloop()
