# Calculator Logic
def Calculator_Logic(self):
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