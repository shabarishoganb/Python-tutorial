from tkinter import *
import random
def guess_the_number():
    def check_guess():
        guess = int(guess_entry.get())
        nonlocal attempts
        attempts += 1
        if guess < target:
            result_label.config(text="Too small, try again.")
        elif guess > target:
            result_label.config(text="Too large, try again.")
        else:
            result_label.config(text=f"Correct! Total guesses: {attempts}")
    target = random.randint(1, 100)
    attempts = 0
    root = Tk()
    root.title("Guess the Number")
    Label(root, text="Enter your guess:").pack()
    guess_entry = Entry(root)
    guess_entry.pack()
    Button(root, text="Check", command=check_guess).pack()
    result_label = Label(root, text="")
    result_label.pack()
    root.mainloop()
guess_the_number()