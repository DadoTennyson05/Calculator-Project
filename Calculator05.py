from tkinter import *
import math

class Genius_Pad(Frame):
# Main class  for the calculator

    def __init__(self, master):
    # Frame of the calculator
        super(Genius_Pad, self).__init__(master)
        self.function = ""
        self.user_input = StringVar()
        self.grid()
        self.calculator_widgets()

    def calculator_widgets(self):
    # Creating the buttons of the calculator and design
    # GUI

        self.input = Entry(self, bg = "gray", bd = 29, 
        insertwidth = 4, width = 30,
        font = ("Arial", 20, "bold"), textvariable = self.user_input, justify = RIGHT)
        self.input.grid(columnspan = 4)

        self.input.insert(0, "0")
        
        # Button for number 0
        self.num0 = Button(self, bg = "white smoke", bd = 12, 
        text = "0",  padx = 35, pady = 25,
        command = lambda : self.click_button(0), font = ("Arial", 20, "bold"))
        self.num0.grid(row = 5, column = 0, sticky = W)
        
        # Button for number 1
        self.num1 = Button(self, bg = "white smoke", bd = 12,
        text = "1", padx = 35, pady = 25, font = ("Arial", 20, "bold"), 
        command = lambda : self.click_button(1))
        self.num1.grid(row = 2, column = 0, sticky = W)

        # Button for number 2
        self.num2 = Button(self, bg = "white smoke", bd = 12, 
        text = "2",  padx = 35, pady = 25, 
        command = lambda : self.click_button(2), font = ("Arial", 20, "bold"))
        self.num2.grid(row = 2, column = 1, sticky = W)
        
        # Button for number 3
        self.num3 = Button(self, bg = "white smoke", bd = 12, 
        text = "3",  padx = 35, pady = 25,
        command = lambda : self.click_button(3), font = ("Arial", 20, "bold"))
        self.num3.grid(row = 2, column = 2, sticky = W)

        # Button for number 4
        self.num4 = Button(self, bg = "white smoke", bd = 12,
        text = "4",  padx = 35, pady = 25,
        command = lambda : self.click_button(4), font = ("Arial", 20, "bold"))
        self.num4.grid(row = 3, column = 0, sticky = W)

        # Button for number 5
        self.num5 = Button(self, bg = "white smoke", bd = 12, 
        text = "5",  padx = 35, pady = 25,
        command = lambda : self.click_button(5), font = ("Arial", 20, "bold"))
        self.num5.grid(row = 3, column = 1, sticky = W)

        # Button for number 6
        self.num6 = Button(self, bg = "white smoke", bd = 12, 
        text = "6",  padx = 35, pady = 25,
        command = lambda : self.click_button(6), font = ("Arial", 20, "bold"))
        self.num6.grid(row = 3, column = 2, sticky = W)

        # Button for number 7
        self.num7 = Button(self, bg = "white smoke", bd = 12, 
        text = "7",  padx = 35, pady = 25, 
        command = lambda : self.click_button(7), font = ("Arial", 20, "bold"))
        self.num7.grid(row = 4, column = 0, sticky = W)

        # Button for number 8
        self.num8 = Button(self, bg = "white smoke", bd = 12, 
        text = "8",  padx = 35, pady = 25,
        command = lambda : self.click_button(8), font = ("Arial", 20, "bold"))
        self.num8.grid(row = 4, column = 1, sticky = W)

        # Button for number 9
        self.num9 = Button(self, bg = "white smoke", bd = 12, 
        text = "9",  padx = 35, pady = 25,
        command = lambda : self.click_button(9), font = ("Arial", 20, "bold"))
        self.num9.grid(row = 4, column = 2, sticky = W)

        # Buttons for basic operations
        # Addition
        self.Addbutton = Button(self, bg = "white smoke", bd = 12, 
        text = "+",  padx = 32, pady = 25,
        command = lambda : self.click_button("+"), font = ("Arial", 20, "bold"), fg = "deep pink")
        self.Addbutton.grid(row = 2, column = 3, sticky = W)

        # Subtraction
        self.Subbutton = Button(self, bg = "white smoke", bd = 12, 
        text = "-",  padx = 36, pady = 25,
        command = lambda : self.click_button("-"), font = ("Arial", 20, "bold"), fg = "deep pink")
        self.Subbutton.grid(row = 3, column = 3, sticky = W)

        # Multiplication
        self.Multbutton = Button(self, bg = "white smoke", bd = 12, 
        text = "*",  padx = 35, pady = 25,
        command = lambda : self.click_button("*"), font = ("Arial", 20, "bold"), fg = "deep pink")
        self.Multbutton.grid(row = 4, column = 3, sticky = W)

        # Division
        self.Divbutton = Button(self, bg = "white smoke", bd = 12, 
        text = "/",  padx = 36, pady = 25,
        command = lambda : self.click_button("/"), font = ("Arial", 20, "bold"), fg = "deep pink")
        self.Divbutton.grid(row = 5, column = 3, sticky = W)

        # Decimal button
        self.Decimalbutton = Button(self, bg = "white smoke", bd = 12, 
        text = ".",  padx = 38, pady = 25,
        command = lambda : self.click_button("."), font = ("Arial", 20, "bold"))
        self.Decimalbutton.grid(row = 5, column = 1, sticky = W)

        # Equal button
        self.Equalbutton = Button(self, bg = "white smoke", bd = 12, 
        text = "=", font = ("Arial", 20, "bold"), padx = 35, pady = 25, command = self.Calculate)
        self.Equalbutton.grid(row = 5, column = 2, sticky = W, columnspan = 2)

        # Clear Button
        self.Clearbutton = Button(self, bg = "white smoke", bd = 12,
        text = "AC", font = ("Arial", 20, "bold"), fg = "deep sky blue", width = 5, padx = 6, command = self.Clear)
        self.Clearbutton.grid(row = 1, column = 3, sticky = W, columnspan = 2)

        # Delete Button
        self.Delbutton = Button(self, bg = "white smoke", bd = 12,
        text = "Del", font = ("Arial", 20, "bold"), fg = "deep sky blue", width = 5, padx = 8, command = self.DeleteNum)
        self.Delbutton.grid(row = 1, column = 2, sticky = W, columnspan = 2)

        # Exponent Button
        self.Expbutton = Button(self, bg = "white smoke", bd = 12,
        text = "x^2", font = ("Arial", 20, "bold"), fg = "deep sky blue", width = 5, padx = 8, command = self.ExpNum)
        self.Expbutton.grid(row = 1, column = 1, sticky = W, columnspan = 2)

        # Squareroot Button
        self.Sqrtbutton = Button(self, bg = "white smoke", bd = 12,
        text = "???", font = ("Verdana", 20, "bold"), fg = "deep sky blue", width = 5, padx = 4, command = self.SqrtNum)
        self.Sqrtbutton.grid(row = 1, column = 0, sticky = W, columnspan = 2)

    def click_button(self, number):
        self.function = str(self.function) + str(number)
        self.user_input.set(self.function)

    # Calculator Logic
    def Calculate(self):
        self.data = self.input.get()
        try:
            self.answer = eval(self.data)
            self.displayResult(self.answer)
            self.function = self.answer

        except SyntaxError as e:
            self.displayResult("Syntax Error")
            self.function = ""

        except ZeroDivisionError:
            self.displayResult("Zero Division Error")
            self.function = ""

    def displayResult(self, value):
        self.input.delete(0, END)
        self.input.insert(0, value)

    def Clear(self):
        self.function = ""
        self.input.delete(0, END)
        self.input.insert(0, "0")

    def DeleteNum(self):
        self.function = self.input.get()[:-1]
        self.input.delete(0, END)
        self.input.insert(0, self.function)

    def ExpNum(self):
        self.function = math.pow(float(self.input.get()), 2)
        self.input.delete(0, END)
        self.input.insert(0, self.function)
        
    def SqrtNum(self):
        self.function = math.sqrt(float(self.input.get()))
        self.input.delete(0, END)
        self.input.insert(0, self.function)

calculator = Tk()

calculator.title("The Genius Pad")
app = Genius_Pad(calculator)
# Make window fixed (cannot be resized)
calculator.resizable(width = False, height = False)

calculator.mainloop()
