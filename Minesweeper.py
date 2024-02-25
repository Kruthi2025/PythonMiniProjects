import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.game_over = False

        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.generate_board()

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game)
        self.new_game_button.pack()

        for i in range(rows):
            for j in range(cols):
                self.buttons[i][j] = tk.Button(self.frame, width=2, height=1)
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].bind('<Button-1>', lambda event, row=i, col=j: self.on_left_click(row, col))
                self.buttons[i][j].bind('<Button-3>', lambda event, row=i, col=j: self.on_right_click(row, col))

    def generate_board(self):
        count = 0
        while count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                count += 1
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    continue
                for r in range(max(0, i - 1), min(self.rows, i + 2)):
                    for c in range(max(0, j - 1), min(self.cols, j + 2)):
                        if self.board[r][c] == -1:
                            self.board[i][j] += 1

    def new_game(self):
        self.game_over = False
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(text="")
                self.buttons[i][j].config(state="normal")
                self.flags[i][j] = False

    def on_left_click(self, row, col):
        if self.game_over or self.flags[row][col]:
            return
        if self.board[row][col] == -1:
            self.game_over = True
            self.reveal_board()
            return
        self.reveal_empty_cells(row, col)

    def reveal_empty_cells(self, row, col):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.board[row][col] != 0:
            return
        if self.buttons[row][col]['state'] == 'normal':
            self.buttons[row][col].config(text=str(self.board[row][col]))
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    self.reveal_empty_cells(r, c)

    def on_right_click(self, row, col):
        if self.game_over:
            return
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col].config(text="F")
            self.flags[row][col] = True
        elif self.buttons[row][col]['text'] == "F":
            self.buttons[row][col].config(text="")
            self.flags[row][col] = False

    def reveal_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j].config(text="*")

def main():
    root = tk.Tk()
    minesweeper = Minesweeper(root, rows=8, cols=8, mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()
