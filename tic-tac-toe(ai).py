import tkinter as tk
import random

class TicTacToeAI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe AI")
        self.board = [" " for _ in range(9)]
        self.turn = "X"
        self.ai_player = "O"

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(master, text=" ", width=8, height=4, command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, row, col):
        if self.board[row*3 + col] == " ":
            self.buttons[row][col].config(text=self.turn)
            self.board[row*3 + col] = self.turn

            if self.check_winner(self.turn):
                print(f"Player {self.turn} wins!")
                self.reset_board()
                return

            if self.check_draw():
                print("It's a draw!")
                self.reset_board()
                return

            self.switch_turn()

            # AI move
            if self.turn == self.ai_player:
                self.make_ai_move()

                if self.check_winner(self.ai_player):
                    print(f"Player {self.ai_player} wins!")
                    self.reset_board()
                    return

                if self.check_draw():
                    print("It's a draw!")
                    self.reset_board()
                    return

                self.switch_turn()

    def make_ai_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == " "]
        if empty_cells:
            move = random.choice(empty_cells)
            row, col = divmod(move, 3)
            self.buttons[row][col].config(text=self.ai_player)
            self.board[move] = self.ai_player

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if (self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] == player) or \
                (self.board[i] == self.board[i+3] == self.board[i+6] == player):
                return True
        if (self.board[0] == self.board[4] == self.board[8] == player) or \
            (self.board[2] == self.board[4] == self.board[6] == player):
            return True
        return False

    def check_draw(self):
        return " " not in self.board

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        self.turn = "X"
        for row in self.buttons:
            for btn in row:
                btn.config(text=" ")

def main():
    root = tk.Tk()
    game = TicTacToeAI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
