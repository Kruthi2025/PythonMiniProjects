import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Guess the number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()
        
    def check_guess(self):
        guess = self.entry.get()
        
        try:
            guess = int(guess)
            self.attempts += 1
            if guess == self.secret_number:
                self.result_label.config(text=f"Correct! You guessed the number in {self.attempts} attempts!")
                self.reset_game()
            elif guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            else:
                self.result_label.config(text="Too high! Try again.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
            
    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
