"""
Tic Tac Toe game.
Task:
Build a two-player game where users take turns to place "X" or
"O" on a 3x3 grid, using buttons or clickable areas.
"""



import tkinter as tk
from tkinter import messagebox

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
current_player = "X"

def create_board():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(cell != " " for row in board for cell in row)

def make_move(row, col, buttons):
    global current_player
    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            disable_buttons(buttons)
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_buttons(buttons)
        else:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
    else:
        messagebox.showwarning("Invalid Move", "This space is already taken!")

def disable_buttons(buttons):
    for row in buttons:
        for button in row:
            button.config(state="disabled")

def reset_game(buttons):
    global board, current_player
    create_board()
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state="normal")

def create_gui(root):
    global board, current_player
    create_board()
    buttons = [[None] * 3 for _ in range(3)]

    
    # Create a 3x3 grid of buttons
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                                      command=lambda i=i, j=j: make_move(i, j, buttons))
            buttons[i][j].grid(row=i, column=j)
    
    # Reset button
    tk.Button(root, text="Play Again", font=("Arial", 12), command=lambda: reset_game(buttons)).grid(row=3, column=0, columnspan=3)

# Running the game
root = tk.Tk()
root.title("Tic Tac Toe")
create_gui(root)
root.mainloop()