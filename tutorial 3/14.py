from tkinter import *
from tkinter import messagebox
import math

# 14. GUI program to compute the square root with error handling
def compute_square_root_with_messagebox():
    def calculate():
        try:
            number = int(input_entry.get())
            if number < 0:
                raise ValueError("Cannot compute square root of a negative number!")
            result = math.sqrt(number)
            messagebox.showinfo("Result", f"Square Root: {result:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    root = Tk()
    root.title("Square Root Calculator")
    
    Label(root, text="Enter an integer:").pack()
    input_entry = Entry(root)
    input_entry.pack()
    
    Button(root, text="Compute", command=calculate).pack()
    
    root.mainloop()

if __name__ == "__main__":
    compute_square_root_with_messagebox()
