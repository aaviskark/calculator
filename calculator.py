#imports
from tkinter import Tk, Button, Entry, END  
import math 

root = Tk()


#setting up the window
root.wm_geometry("432x225")
root.title("Calculator")
root.resizable(0,0)

#setting up the textbox
box = Entry(root, width = 35, borderwidth = 2)
box.grid(row = 0, column = 0, columnspan = 6, pady = 10)


#different functions for the calculator
def addition():
    global first_number
    global function
    first_number = box.get()
    function = "addition"
    first_number = int(first_number)
    box.delete(0, END)

def subtraction():
    global first_number
    global function
    first_number = box.get()
    function = "subtraction"
    first_number = int(first_number)
    box.delete(0, END)

def multiplication():
    global first_number
    global function
    first_number = box.get()
    function = "multiplication"
    first_number = int(first_number)
    box.delete(0, END)

def division():
    global first_number
    global function
    first_number = box.get()
    function = "division"
    first_number = int(first_number)
    box.delete(0, END)

#special functions that act differently
def special_function(func):
    if func == "sqrt":
        sq_number = box.get()
        sq_num = math.sqrt(float(sq_number))
        box.delete(0, END)
        box.insert(0, sq_num)
    elif func == "factorial":
        fac_number = box.get()
        f_num = math.factorial(float(fac_number))
        box.delete(0, END)
        box.insert(0, f_num)
    

# functions for the text box         
def action(number):     #makes it able to insert multiple numbers into the box
    current = box.get()
    box.delete(0, END)
    box.insert(0, str(current) + str(number))

def clearall():
    box.delete(0, END)

def answer():
    second_number = box.get()
    box.delete(0, END)
    if function == "addition":
       box.insert(0, first_number + float(second_number)) 
    elif function == "subtraction":
        box.insert(0, first_number - float(second_number))
    elif function == "multiplication":
        box.insert(0, first_number * float(second_number))
    elif function == "division":  
        box.insert(0, first_number / float(second_number))

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
Button(root, text = "=", width = 15, command = answer).grid(row= 2, column = 5)
Button(root, text = "AC", width = 15, command = clearall).grid(row = 1, column = 5)

Button(root, text = "+", width = 10, command = addition).grid(row = 1, column = 4)
Button(root, text = "-", width = 10, command = subtraction).grid(row = 2, column = 4)
Button(root, text = "x", width = 10, command = multiplication).grid(row = 3, column = 4)
Button(root, text = "/", width = 10, command = division).grid(row = 4, column = 4)

Button(root, text = "!", width = 10, command = lambda: special_function("factorial")).grid(row= 4, column = 1)
Button(root, text = "√", width = 10, command = lambda: special_function("sqrt")).grid(row = 4, column = 2)


root.mainloop()
