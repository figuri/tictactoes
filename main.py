# Import the tkinter library for creating the graphical interface
import tkinter as tk
# Import messagebox submodule from tkinter for displaying message boxes
from tkinter import messagebox

# Define a class for the Tic Tac Toe game, inheriting from the tkinter window
class TicTacToe(tk.Tk):
    # Constructor method initializes the game when an object is created
    def __init__(self):
        # Call the constructor of the parent class (tk.Tk) to create the game window
        super().__init__()
        # Set the title of the game window
        self.title("Tic Tac Toe")
        # Initialize the current player as "X"
        self.current_player = "X"
        # Create a 3x3 game board represented as a matrix of empty strings
        self.board = [["" for _ in range(3)] for _ in range(3)]
        # Create a matrix of buttons for the Tic Tac Toe grid, initially set to None
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        # Call the create_grid() method to create the GUI grid of buttons
        self.create_grid()

    # Method to create the graphical grid of buttons for the game
    def create_grid(self):
        # Nested loops to create a 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                # Create a button at position (i, j) with specified properties
                self.buttons[i][j] = tk.Button(self, text="", font=("Arial", 24), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                # Place the button in the grid at row i and column j
                self.buttons[i][j].grid(row=i, column=j)

    # Method called when a button is clicked
    def on_button_click(self, i, j):
        # Check if the clicked cell is empty and there is no winner yet
        if self.board[i][j] == "" and not self.check_winner():
            # Set the clicked cell to the current player's marker ("X" or "O")
            self.board[i][j] = self.current_player
            # Update the text of the clicked button to display the player's marker
            self.buttons[i][j].config(text=self.current_player)
            # Check for a winner or a tie
            if self.check_winner():
                # If there is a winner, display a message box with the winner's name
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                # Reset the game
                self.reset_game()
            elif self.is_board_full():
                # If the board is full and there is no winner, it's a tie
                messagebox.showinfo("Game Over", "It's a tie!")
                # Reset the game
                self.reset_game()
            else:
                # If the game is still ongoing, switch to the other player's turn
                self.switch_player()

    # Method to switch the current player between "X" and "O"
    def switch_player(self):
        # Change the current player from "X" to "O" or from "O" to "X"
        self.current_player = "O" if self.current_player == "X" else "X"

    # Method to check if there is a winner on the game board
    def check_winner(self):
        # Check rows for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
        # Check columns for a win
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return True
        # Check diagonals for a win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        # If no winner, return False
        return False

    # Method to check if the game board is full (a tie)
    def is_board_full(self):
        # Iterate through the board and check if there are any empty cells
        for i in range(3):
            for j in range(3):
                # If an empty cell is found, the board is not full, return False
                if self.board[i][j] == "":
                    return False
        # If no empty cells are found, the board is full, return True
        return True

    # Method to reset the game board and buttons to their initial state
    def reset_game(self):
        # Reset the board to an empty state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        # Reset the text of all buttons to empty strings
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        # Reset the current player to "X" for the next game
        self.current_player = "X"

# Main block: create an instance of the TicTacToe class and start the GUI event loop
if __name__ == "__main__":
    # Create an object of the TicTacToe class
    app = TicTacToe()
    # Start the graphical user interface event loop
    app.mainloop()
