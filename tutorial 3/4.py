from tkinter import *
def temperature_converter():
    def f_to_c():
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_entry.delete(0, END)
        celsius_entry.insert(0, f"{celsius:.2f}")

    def c_to_f():
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_entry.delete(0, END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.2f}")

    root = Tk()
    root.title("Temperature Converter")
    Label(root, text="Fahrenheit").grid(row=0, column=0)
    Label(root, text="Celsius").grid(row=0, column=1)
    fahrenheit_entry = Entry(root)
    fahrenheit_entry.grid(row=1, column=0)
    fahrenheit_entry.insert(0, "32")
    celsius_entry = Entry(root)
    celsius_entry.grid(row=1, column=1)
    celsius_entry.insert(0, "0.0")
    Button(root, text=">>>>", command=f_to_c).grid(row=2, column=0)
    Button(root, text="<<<<", command=c_to_f).grid(row=2, column=1)
    root.mainloop()
temperature_converter()