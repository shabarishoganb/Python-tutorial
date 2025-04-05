from tkinter import *
import math
def compute_square_root():
    def calculate():
        try:
            number = int(input_entry.get())
            result_label.config(text=f"Square Root: {math.sqrt(number):.2f}")
        except ValueError:
            result_label.config(text="Invalid input!")
    root = Tk()
    root.title("Square Root Calculator")
    input_entry = Entry(root)
    input_entry.pack()
    Button(root, text="Compute", command=calculate).pack()
    result_label = Label(root, text="")
    result_label.pack()
    root.mainloop()
compute_square_root()