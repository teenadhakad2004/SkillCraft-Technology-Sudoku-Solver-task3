import tkinter as tk
from tkinter import messagebox

# Sudoku Solver Logic (Backtracking)
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Check if initial board is valid
def is_valid_board(board):
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                if not is_valid(board, row, col, num):
                    return False
                board[row][col] = num
    return True

# GUI Functions
def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board

def display_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))

def solve():
    board = get_board()
    if not is_valid_board(board):
        messagebox.showerror("Invalid Puzzle", "The given Sudoku puzzle is invalid!")
        return

    if solve_sudoku(board):
        display_board(board)
        messagebox.showinfo("Success", "Sudoku Solved Successfully!")
    else:
        messagebox.showerror("No Solution", "This Sudoku puzzle cannot be solved.")

def clear_grid():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# Tkinter Window
root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg="#1e1e2f")

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

entries = [[None for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        e = tk.Entry(frame, width=3, font=("Arial", 16), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        entries[i][j] = e

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

solve_btn = tk.Button(btn_frame, text="Solve", command=solve, bg="#4CAF50", fg="white", font=("Arial", 12))
solve_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", command=clear_grid, bg="#f44336", fg="white", font=("Arial", 12))
clear_btn.grid(row=0, column=1, padx=10)

root.mainloop()
