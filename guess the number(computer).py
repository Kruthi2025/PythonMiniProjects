import tkinter as tk
import random

def guess_number():
    guess = int(guess_entry.get())
    global attempts_remaining
    attempts_remaining -= 1
    attempts_label.config(text=f"Attempts Remaining: {attempts_remaining}")

    if guess == computer_number:
        result_label.config(text="You guessed it! Congratulations!")
        guess_button.config(state=tk.DISABLED)
    elif guess < computer_number:
        result_label.config(text="Too low. Try again.")
    else:
        result_label.config(text="Too high. Try again.")

    if attempts_remaining == 0:
        result_label.config(text="Out of attempts! The number was:", font=("Arial", 12, "bold"))
        number_label.config(text=computer_number, font=("Arial", 12, "bold"))
        guess_button.config(state=tk.DISABLED)

def new_game():
    global computer_number, attempts_remaining
    computer_number = random.randint(1, 100)
    attempts_remaining = 10
    guess_entry.delete(0, tk.END)
    result_label.config(text="")
    number_label.config(text="")
    guess_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Guess the Number")

computer_number = random.randint(1, 100)
attempts_remaining = 10

instruction_label = tk.Label(root, text="I'm thinking of a number between 1 and 100. Guess it!")
instruction_label.pack()

attempts_label = tk.Label(root, text=f"Attempts Remaining: {attempts_remaining}")
attempts_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_number)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

number_label = tk.Label(root, text="")
number_label.pack()

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack()

root.mainloop()
