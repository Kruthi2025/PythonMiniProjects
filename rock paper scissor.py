import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Select your choice:")
        self.label.pack()
        
        self.rock_button = tk.Button(self.master, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack()
        
        self.paper_button = tk.Button(self.master, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack()
        
        self.scissors_button = tk.Button(self.master, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack()
        
    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)
        messagebox.showinfo("Result", result)
        
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return f"Both chose {user_choice}. It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return f"You chose {user_choice} and computer chose {computer_choice}. You win!"
        else:
            return f"You chose {user_choice} and computer chose {computer_choice}. Computer wins!"

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
