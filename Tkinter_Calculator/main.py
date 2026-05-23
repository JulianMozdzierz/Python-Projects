import tkinter as tk

window = tk.Tk()
window.title("Calculator") 

class Calculator:
    def __init__(self, win):
        self.equationStrVar = tk.StringVar()
        self.expressionStr = ""
        self.calcKeyboard = [
            ["7","8","9","+"],
            ["4","5","6","-"],
            ["1","2","3","*"],
            ["0","Clear", "=", "/"]
        ]
        self.prepareGui(win)
        
    def prepareGui(self, win):
        win.geometry("260x130")
        self.expressionField = tk.Entry(win, textvariable=self.equationStrVar)
        self.expressionField.grid(columnspan=4, ipadx=60)
        
        rowIndex = 0
        while rowIndex < len(self.calcKeyboard):
            calcRow = self.calcKeyboard[rowIndex]

            columnIndex = 0
            while columnIndex < len(calcRow):
                buttonText = calcRow[columnIndex]
                button = tk.Button(win, text=buttonText, height= 1, width=8, fg="black", 
                                   bg="silver", command=lambda v = buttonText: self.buttonPressed(v))
                button.grid(row = rowIndex + 1, column = columnIndex)
                columnIndex+=1

            rowIndex +=1
        
    def buttonPressed(self, value):
        print("button pressed: ", value)

        if value == "Clear":
            self.expressionStr = ""
            self.equationStrVar.set("")
            return
        
        if value == "=":
            result = str( eval(self.expressionStr) )
            self.expressionStr = result
            self.equationStrVar.set(result)
            return 
        
        self.expressionStr += str(value)
        self.equationStrVar.set(self.expressionStr)

calc=Calculator(window)


window.mainloop()