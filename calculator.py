#imports
from tkinter import Tk, Button, Entry, END  
import math 

root = Tk()


#setting up the window
root.wm_geometry("400x450")
root.title("Calculator")
root.resizable(0,0)

#setting up the textbox
box = Entry(root, width = 35, borderwidth = 2)
box.grid(row = 0, column = 0, columnspan = 6, pady = 10)
# box.insert(0, '0.0')

def replace():
    box.txt = box.get() 
    box.txt = box.txt.replace('÷', '/')
    box.txt = box.txt.replace('x', '*')
    box.txt = box.txt.replace('%', '/100')

#different functions for the calculator
def addition(x,y):
    return x + y
def subtraction(x,y):
    return x - y
def multiplication(x,y):
    return x * y 
def division(x,y):
    return x / y

def sqroot(x):
    return math.sqrt(x)
def factorial(x):
    return math.factorial(x)

def specialfunction(specfunc):
    if specfunc == 'sqroot':
        return math.sqrt(float(box.txt))

# functions for the text box         
def action(number):
    current = box.get()
    box.delete(0, END)
    box.insert(0, str(current) + str(number))

def clearall():
    box.delete(0, END)

def answer():
    return

#the number buttons
Button(root, text = "1", width = 10, command = lambda: action(1)).grid(row = 3, column = 0)
Button(root, text = "2", width = 10, command = lambda: action(2)).grid(row = 3, column = 1)
Button(root, text = "3", width = 10, command = lambda: action(3)).grid(row = 3, column = 2)

Button(root, text = "4", width = 10, command = lambda: action(4)).grid(row = 2, column = 0)
Button(root, text = "5", width = 10, command = lambda: action(5)).grid(row = 2, column = 1)
Button(root, text = "6", width = 10, command = lambda: action(6)).grid(row = 2, column = 2)

Button(root, text = "7", width = 10, command = lambda: action(7)).grid(row = 1, column = 0,)
Button(root, text = "8", width = 10, command = lambda: action(8)).grid(row = 1, column = 1)
Button(root, text = "9", width = 10, command = lambda: action(9)).grid(row = 1, column = 2)

Button(root, text = "0", width = 10, command = lambda: action(0)).grid(row = 4, column = 0)

#other buttons 
Button(root, text = "=", width = 20, command = lambda: action(1), padx = 4, pady = 4).grid(row= 4, column = 6)
Button(root, text = "AC", width = 10, command = clearall, padx = 4, pady = 4).grid(row = 1, column = 4)

Button(root, text = "!", width = 10, command = lambda: action(1)).grid(row= 4, column = 1)
Button(root, text = "√", width = 10, command = lambda: specialfunction('sqroot')).grid(row = 4, column = 2)


root.mainloop()
