import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.words = ["python", "hangman", "programming", "computer", "keyboard", "mouse", "monitor", "software"]
        self.secret_word = random.choice(self.words)
        self.guesses_left = len(HangmanGame.HANGMAN_PARTS) - 1  # Excluding the base
        self.guessed_letters = set()
        
        self.create_widgets()
        self.draw_hangman()
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()
        
        self.word_label = tk.Label(self.master, text=self.display_word())
        self.word_label.pack()
        
        self.label = tk.Label(self.master, text=f"Guesses left: {self.guesses_left}")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
    def draw_hangman(self):
        for i, part in enumerate(HangmanGame.HANGMAN_PARTS):
            if i < len(HangmanGame.HANGMAN_PARTS) - self.guesses_left:
                self.canvas.create_line(part, width=3, fill="black")
            else:
                self.canvas.create_line(part, width=3)
        
    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.secret_word)
        
    def check_guess(self):
        guess = self.entry.get().lower()
        
        if len(guess) != 1 or not guess.isalpha():
            self.label.config(text="Please enter a single letter.")
        elif guess in self.guessed_letters:
            self.label.config(text="You've already guessed this letter.")
        else:
            self.guessed_letters.add(guess)
            if guess not in self.secret_word:
                self.guesses_left -= 1
                self.label.config(text=f"Guesses left: {self.guesses_left}")
                
                if self.guesses_left == 0:
                    self.label.config(text=f"Sorry, you're out of guesses. The word was '{self.secret_word}'.")
                    self.reset_game()
            else:
                self.word_label.config(text=self.display_word())
                if self.all_letters_guessed():
                    if guess == self.secret_word:
                        self.label.config(text=f"Congratulations! You've guessed the word '{self.secret_word}'.")
                        self.reset_game()
        
    def all_letters_guessed(self):
        return set(self.secret_word) == self.guessed_letters
        
    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guesses_left = len(HangmanGame.HANGMAN_PARTS) - 1
        self.guessed_letters = set()
        self.word_label.config(text=self.display_word())
        self.label.config(text=f"Guesses left: {self.guesses_left}")
        self.entry.delete(0, tk.END)
        self.canvas.delete("all")
        self.draw_hangman()
        
    HANGMAN_PARTS = [
        (50, 280, 250, 280),   # base
        (150, 50, 150, 280),   # pole
        (140, 50, 150, 70),    # beam
        (140, 70, 200, 70),    # rope
        (200, 70, 200, 100),   # head
        (200, 100, 200, 200),  # body
        (200, 125, 175, 100),  # left arm
        (200, 125, 225, 100),  # right arm
        (200, 200, 175, 250),  # left leg
        (200, 200, 225, 250)   # right leg
    ]

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
