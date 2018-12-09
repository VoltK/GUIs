from tkinter import Tk, DoubleVar, StringVar, END
from tkinter import messagebox
from tkinter.ttk import *


class Calc:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        #self.master.geometry("400x300")
        self.master.bind('<Return>', self.get_field)

        self.total = 0
        self.total_var = DoubleVar()
        self.total_var.set(self.total)

        self.expression = ''
        self.exp = StringVar()
        self.exp_label = Label(self.master, textvariable=self.exp)
        self.exp_label.grid(row=0, column=0)

        self.total_label = Label(self.master, textvariable=self.total_var)
        self.total_label.grid(row=0, column=1)

        # optional input field
        self.enter = Entry(self.master)
        self.enter.grid(row=1, column=1)

        # creating operation buttons
        self.plus = Button(self.master, text='+', command=lambda: self.update('+'))
        self.plus.grid(row=4, column=3)

        self.minus = Button(self.master, text='-', command=lambda: self.update('-'))
        self.minus.grid(row=5, column=3)

        self.multiply = Button(self.master, text='*', command=lambda: self.update('*'))
        self.multiply.grid(row=2, column=3)

        self.divide = Button(self.master, text='/', command=lambda: self.update('/'))
        self.divide.grid(row=3, column=3)

        self.delete = Button(self.master, text='del', command=lambda: self.update('del'))
        self.delete.grid(row=1, column=2)

        self.mod = Button(self.master, text='%', command=lambda: self.update('%'))
        self.mod.grid(row=5, column=2)

        self.exponent = Button(self.master, text='^', command=lambda: self.update('**'))
        self.exponent.grid(row=6, column=2)

        self.dot = Button(self.master, text='.', command=lambda: self.update('.'))
        self.dot.grid(row=5, column=1)

        self.equal = Button(self.master, text='=', command=lambda: self.update('='))
        self.equal.grid(row=6, column=3)

        self.reset = Button(self.master, text='C', command=lambda: self.update('C'))
        self.reset.grid(row=1, column=3)

        # start with 2 row and default column
        row = 2
        column = 0
        # create 9 integers buttons
        for num in range(10):
            # add function to every button, on press -> add number to expression
            number = Button(self.master, text=str(num), command=lambda num=num: self.update(str(num)))
            number.grid(row=row, column=column)
            # numbers will be in 3 columns if it's third column -> move to next row
            if column == 2:
                column = 0
                row += 1
            else:
                column += 1

    def get_field(self, event):
        # in input field empty we use existing total
        if self.enter.get() == "":
            self.expression += str(self.total)
        # if input start with operation -> use existing total as first number
        elif self.enter.get()[0] in "+-/*%":
            self.expression = str(self.total_var.get()) + self.enter.get()
        else:
            self.expression += self.enter.get()

        self.exp.set(self.expression)
        self.enter.delete(0, END)

    def update(self, char):
        # clear all
        if char == 'C':
                self.expression = ""
                self.total = 0
        # delete last element from expression
        elif char == "del":
            self.expression = self.expression[:-1]

        elif char == '=':
            try:
                # evaluate expression
                self.total = eval(self.expression)
                self.expression = ""
            except NameError:
                messagebox.showerror("Error", "You entered character")
            except ZeroDivisionError:
                messagebox.showerror("Error", "You cannot divide by zero")
        else:
            # add value to expression
                self.expression += char
            # if expression start with operation -> use existing total as first number
                if self.expression[0] in "+-/*%":
                        self.expression = str(float(self.total_var.get())) + self.expression

        self.exp.set(self.expression)
        self.total_var.set(self.total)
        self.enter.delete(0, END)


root = Tk()
calc = Calc(root)
root.mainloop()