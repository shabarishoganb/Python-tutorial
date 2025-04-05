from tkinter import *
def bouncy_ball_distance():
    def calculate():
        h = float(height_entry.get())
        b = float(bounciness_entry.get())
        n = int(bounce_entry.get())
        total_distance = 0
        for _ in range(n):
            total_distance += h + h * b
            h *= b
        result_label.config(text=f"Total Distance: {total_distance:.2f}")
    root = Tk()
    root.title("Bouncy Ball Distance Calculator")
    Label(root, text="Initial Height:").pack()
    height_entry = Entry(root)
    height_entry.pack()
    Label(root, text="Bounciness Index:").pack()
    bounciness_entry = Entry(root)
    bounciness_entry.pack()
    Label(root, text="Number of Bounces:").pack()
    bounce_entry = Entry(root)
    bounce_entry.pack()
    Button(root, text="Calculate", command=calculate).pack()
    result_label = Label(root, text="")
    result_label.pack()
    root.mainloop()
bouncy_ball_distance()