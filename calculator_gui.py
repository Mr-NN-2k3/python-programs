from tkinter import *

# Initialize the main window
root = Tk()
root.title("calculator")
root.geometry("640x760")
root.resizable(0, 0)
root.config(bg="black")

# Global variables to store the first operand and the operation
first_operand = ""
operation = ""

# Function to clear the display and reset the operands and operation
def clear_src():
    global first_operand, operation
    first_operand = ""
    operation = ""
    display.config(text="")

# Function to set the operation and store the first operand
def set_operation(op):
    global first_operand, operation
    first_operand = display.cget("text")
    operation = op
    display.config(text="")

# Function to calculate the result based on the operation and operands
def calculate_result():
    global first_operand, operation
    second_operand = display.cget("text")
    try:
        if operation == "+":
            result = float(first_operand) + float(second_operand)
        elif operation == "-":
            result = float(first_operand) - float(second_operand)
        elif operation == "*":
            result = float(first_operand) * float(second_operand)
        elif operation == "/":
            result = float(first_operand) / float(second_operand)

        # Write the calculation to a file
        with open("calculator_db.txt" , "a+") as f:#add the location here
            f.write(f"{first_operand} {operation} {second_operand} = {result} \n")

        display.config(text=str(result))
    except (ValueError, ZeroDivisionError):
        display.config(text="Error")
    first_operand = ""
    operation = ""

# Function to append a digit to the current number on the display
def value(digit):
    current = display.cget("text")
    if len(current) < 21:  # Limit input to 21 digits
        new = current + str(digit)
        display.config(text=new)

# Display label to show the current number and results
display = Label(root, text="", background="black", foreground="white")
display.grid(row=0, column=0, pady=(0, 70), ipady=10, columnspan=5, sticky="w")
display.config(font=("verdana", 30))

# Create digit buttons (0-9) and assign the value function to them
btn7 = Button(root, text=7, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(7))
btn7.grid(row=1, column=0)
btn7.config(font=("verdana"))

btn8 = Button(root, text=8, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(8))
btn8.grid(row=1, column=1)
btn8.config(font=("verdana"))

btn9 = Button(root, text=9, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(9))
btn9.grid(row=1, column=2)
btn9.config(font=("verdana"))

btn4 = Button(root, text=4, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(4))
btn4.grid(row=2, column=0)
btn4.config(font=("verdana"))

btn5 = Button(root, text=5, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(5))
btn5.grid(row=2, column=1)
btn5.config(font=("verdana"))

btn6 = Button(root, text=6, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(6))
btn6.grid(row=2, column=2)
btn6.config(font=("verdana"))

btn1 = Button(root, text=1, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(1))
btn1.grid(row=3, column=0)
btn1.config(font=("verdana"))

btn2 = Button(root, text=2, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(2))
btn2.grid(row=3, column=1)
btn2.config(font=("verdana"))

btn3 = Button(root, text=3, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(3))
btn3.grid(row=3, column=2)
btn3.config(font=("verdana"))

btn0 = Button(root, text=0, bg="orange", fg="white",
              width=15, height=8, command=lambda: value(0))
btn0.grid(row=4, column=0)
btn0.config(font=("verdana"))

# Create operational buttons and assign their respective functions
btn_equal = Button(root, text="=", bg="orange", fg="white",
                   width=15, height=8, command=calculate_result)
btn_equal.grid(row=4, column=1)
btn_equal.config(font=("verdana"))

btn_mul = Button(root, text="*", bg="orange", fg="white",
                 width=15, height=8, command=lambda: set_operation("*"))
btn_mul.grid(row=1, column=3)
btn_mul.config(font=("verdana"))

btn_sub = Button(root, text="-", bg="orange", fg="white",
                 width=15, height=8, command=lambda: set_operation("-"))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=("verdana"))

btn_divide = Button(root, text="/", bg="orange", fg="white",
                    width=15, height=8, command=lambda: set_operation("/"))
btn_divide.grid(row=3, column=3)
btn_divide.config(font=("verdana"))

btn_add = Button(root, text="+", bg="orange", fg="white",
                 width=15, height=8, command=lambda: set_operation("+"))
btn_add.grid(row=4, column=3)
btn_add.config(font=("verdana"))

btn_clear = Button(root, text="C", bg="orange", fg="white",
                   width=15, height=8, command=clear_src)
btn_clear.grid(row=4, column=2)
btn_clear.config(font=("verdana"))

# Run the main event loop
root.mainloop()
