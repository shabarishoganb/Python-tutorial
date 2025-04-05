from tkinter import *
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
string_to_uppercase()