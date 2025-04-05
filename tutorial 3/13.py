from tkinter import *
import math

# 13. GUI program to compute and display the square root of an input number
def compute_square_root():
    def calculate():
        try:
            number = float(input_entry.get())
            result_label.config(text=f"Square Root: {math.sqrt(number):.2f}")
        except ValueError:
            result_label.config(text="Invalid input! Please enter a number.")
    
    root = Tk()
    root.title("Square Root Calculator")
    
    input_entry = Entry(root)
    input_entry.pack()
    
    Button(root, text="Compute", command=calculate).pack()
    
    result_label = Label(root, text="")
    result_label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    compute_square_root()
