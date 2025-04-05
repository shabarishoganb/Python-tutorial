from tkinter import *

# 12. GUI program to convert an input string to uppercase
def string_to_uppercase():
    def convert():
        result_label.config(text=input_entry.get().upper())
    
    root = Tk()
    root.title("Uppercase Converter")
    
    input_entry = Entry(root)
    input_entry.pack()
    
    Button(root, text="Convert", command=convert).pack()
    
    result_label = Label(root, text="")
    result_label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    string_to_uppercase()
