from tkinter import *
import sys

root = Tk()

label_1 = Label(root, text="Values:")
input = Entry(root)
addition = Button(root, text="  Add  ")
subtract = Button(root, text="Subtract")
multiply = Button(root, text="Multiply")
division = Button(root, text="Divide")
equal = Button(root, text="  =  ")
output = Label(root, text="")

label_1.grid(row=0, column=0,sticky=W)
input.grid(row=0, column=1, columnspan=4,sticky=W+E+N+S)

addition.grid(row=1, column=0)
subtract.grid(row=1, column=1)
multiply.grid(row=1, column=2)
division.grid(row=1, column=3)
equal.grid(row=1, column=4)
output.grid(row=2)

input_str = ''

def add(event):
    global input_str
    global input
    input_str += input.get() + '+'
    output.config(text=input_str)
    input = Entry(root, text="")
    input.grid(row=0, column=1, columnspan=3, sticky=W + E + N + S)

def sub(event):
    global input_str
    global input
    input_str += input.get() + '-'
    output.config(text=input_str)
    input = Entry(root, text="")
    input.grid(row=0, column=1, columnspan=3, sticky=W + E + N + S)

def mul(event):
    global input_str
    global input
    input_str += input.get() + 'x'
    output.config(text=input_str)
    input = Entry(root, text="")
    input.grid(row=0, column=1, columnspan=3, sticky=W + E + N + S)

def div(event):
    global input_str
    global input
    input_str += input.get() + '÷'
    output.config(text=input_str)
    input = Entry(root, text="")
    input.grid(row=0, column=1, columnspan=3, sticky=W + E + N + S)

def eq(event):
    global input_str
    input_str = input_str.replace('x', '*')
    input_str = input_str.replace('÷', '/')
    string = input_str[0:len(input_str)-1]
    calculation = str(eval(string))
    calc = calculation
    input_str = ''
    output.config(text=calc)

addition.bind("<Button-1>", add)
subtract.bind("<Button-1>", sub)
multiply.bind("<Button-1>", mul)
division.bind("<Button-1>", div)
equal.bind("<Button-1>", eq)

root.mainloop()