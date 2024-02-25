import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid = [[tk.StringVar() for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(root, width=3, font=('Arial', 16), justify='center', textvariable=self.grid[i][j])
                entry.grid(row=i, column=j)
                entry.bind('<FocusIn>', self.clear_cell)
                entry.bind('<Key>', self.validate_input)

        solve_button = tk.Button(root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4, pady=10)

    def clear_cell(self, event):
        event.widget.delete(0, 'end')

    def validate_input(self, event):
        key = event.char
        if not key.isdigit() or not 1 <= int(key) <= 9:
            event.widget.delete(0, 'end')
            messagebox.showinfo("Invalid Input", "Please enter a digit between 1 and 9.")

    def solve_sudoku(self):
        puzzle = [[int(cell.get()) if cell.get() else 0 for cell in row] for row in self.grid]
        if self.solve(puzzle):
            for i in range(9):
                for j in range(9):
                    self.grid[i][j].set(puzzle[i][j])
        else:
            messagebox.showinfo("No Solution", "No solution exists for the given Sudoku.")

    def is_valid(self, puzzle, row, col, num):
        for i in range(9):
            if puzzle[row][i] == num or puzzle[i][col] == num or puzzle[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
                return False
        return True

    def solve(self, puzzle):
        empty = self.find_empty_cell(puzzle)
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if self.is_valid(puzzle, row, col, num):
                puzzle[row][col] = num
                if self.solve(puzzle):
                    return True
                puzzle[row][col] = 0

        return False

    def find_empty_cell(self, puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return i, j
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
