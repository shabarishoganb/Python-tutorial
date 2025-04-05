from tkinter import *
def computer_guess_number():
    def too_small():
        nonlocal low
        low = mid + 1
        make_guess()
    def too_large():
        nonlocal high
        high = mid - 1
        make_guess()
    def correct():
        result_label.config(text=f"Computer guessed it in {attempts} attempts!")
        disable_buttons()
    def disable_buttons():
        small_button.config(state=DISABLED)
        large_button.config(state=DISABLED)
        correct_button.config(state=DISABLED)
    def make_guess():
        nonlocal mid, attempts
        if low <= high:
            mid = (low + high) // 2
            result_label.config(text=f"Computer guesses: {mid}")
            attempts += 1
    root = Tk()
    root.title("Computer Guesses the Number")
    low, high, attempts = 1, 100, 0
    mid = (low + high) // 2
    result_label = Label(root, text=f"Computer guesses: {mid}")
    result_label.pack()
    small_button = Button(root, text="Too Small", command=too_small)
    large_button = Button(root, text="Too Large", command=too_large)
    correct_button = Button(root, text="Correct", command=correct)
    small_button.pack()
    large_button.pack()
    correct_button.pack()
    root.mainloop()
computer_guess_number()