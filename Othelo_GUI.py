import tkinter as tk
from tkinter import messagebox, simpledialog
from Controller import Controller

class OthelloGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Othello")

        self.controller = None

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.player_vs_player_btn = tk.Button(self.button_frame, text="Player vs Player",
                                              command=self.not_available)
        self.player_vs_player_btn.pack(side=tk.LEFT, padx=5)

        self.player_vs_computer_btn = tk.Button(self.button_frame, text="Player vs Computer",
                                                command=self.start_player_vs_computer)
        self.player_vs_computer_btn.pack(side=tk.LEFT, padx=5)

    def start_player_vs_player(self):
        messagebox.showinfo("Player vs Player", "Player vs Player mode is not available.")

    def start_player_vs_computer(self):
        self.root.withdraw()  # Hide the main window

        depth = simpledialog.askinteger("Depth Selection",
                                        "Enter the desired depth (1 for simple, 3 for moderate, 5 for hard):",
                                        parent=self.root, minvalue=1, maxvalue=5)
        if depth is None:
            self.root.deiconify()  # Show the main window if the dialog is closed
            return

        self.controller = Controller(depth)
        self.clear_valid_moves()
        self.update_board()
        self.player_vs_player_btn.config(state=tk.DISABLED)
        self.player_vs_computer_btn.config(state=tk.DISABLED)

        root = tk.Toplevel()  # Create a new window
        root.protocol("WM_DELETE_WINDOW", self.on_close_game)  # Define behavior on window close
        app = OthelloGame(root, self.controller)

    def on_close_game(self):
        self.controller = None
        self.player_vs_player_btn.config(state=tk.NORMAL)
        self.player_vs_computer_btn.config(state=tk.NORMAL)
        self.root.deiconify()  # Show the main window

    def clear_valid_moves(self):
        pass

    def update_board(self):
        pass

    def not_available(self):
        messagebox.showinfo("Not Available", "Player vs Player mode is not available at the moment.")


class OthelloGame:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Othello")

        # Colors for pieces and valid moves
        self.color_map = {'.': 'green', 'w': 'white', 'b': 'black', 'valid': 'lightgreen'}

        # Create board GUI
        self.create_board()

        self.root.mainloop()

    def create_board(self):
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()

        self.cells = [[None] * 8 for _ in range(8)]

        for i in range(8):
            for j in range(8):
                cell = tk.Label(self.board_frame, text='', width=3, height=1, font=('Arial', 20), relief=tk.RIDGE)
                cell.grid(row=i, column=j)
                cell.bind('<Button-1>', lambda e, x=i, y=j: self.cell_clicked(x, y))
                self.cells[i][j] = cell

        self.update_board()

    def update_board(self):
        board = self.controller.board
        for i in range(8):
            for j in range(8):
                cell_value = board[i][j]
                cell_color = self.color_map[cell_value]
                self.cells[i][j].config(text='', bg=cell_color)

        # Display available moves
        valid_moves = self.controller.getValidMoves(1)
        for move in valid_moves:
            x, y = move
            self.cells[x - 1][y - 1].config(text='●')

    def cell_clicked(self, x, y):
        if self.controller.make_move(x + 1, y + 1, 1):  # Add 1 to x and y to convert to one-based index
            self.clear_valid_moves()
            self.update_board()
            self.check_game_over()
            # Computer's turn if player vs computer mode
            if isinstance(self.controller, Controller) and self.controller.__class__.__name__ == "Controller":
                self.computer_turn()

    def clear_valid_moves(self):
        for i in range(8):
            for j in range(8):
                if self.cells[i][j]['text'] == '●':
                    self.cells[i][j].config(text='')

    def check_game_over(self):
        if not self.controller.getValidMoves(0) and not self.controller.getValidMoves(1):
            white_score = self.controller.PlayerScores[0]
            black_score = self.controller.PlayerScores[1]
            if white_score == black_score:
                messagebox.showinfo("Game Over", "It's a tie!")
            elif white_score > black_score:
                messagebox.showinfo("Game Over", "Player (white) wins!")
            else:
                messagebox.showinfo("Game Over", "Player (black) wins!")
        elif not self.controller.getValidMoves(1):  # No valid moves for current player
            messagebox.showinfo("No Valid Moves", "No valid moves available. Skipping turn.")
            if isinstance(self.controller, Controller) and self.controller.__class__.__name__ == "Controller":
                self.computer_turn()

    def computer_turn(self):
        _, best_move = self.controller.minimax(self.controller, self.controller.depth, float('-inf'), float('inf'),
                                               True)
        if best_move:
            self.controller.board = best_move.board
            self.controller.PlayerScores = best_move.PlayerScores
            self.clear_valid_moves()
            self.update_board()
            self.check_game_over()


if __name__ == '__main__':
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()
