class Controller:

    # player 0 is white
    # player 1 is black
    # the indices used are one-based


    def __init__(self, depth=None):
        self.depth = depth
        self.board = [['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', 'w', 'b', '.', '.', '.'],
                      ['.', '.', '.', 'b', 'w', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.']]
        self.PlayerScores = [2, 2]

        def set_depth(self, depth):
            self.depth = depth

    # returns the moves the player is able to make
    def getValidMoves(self, player):
        moves = []
        for i in range(1, 9):
            for j in range(1, 9):
                if self.validateMove(i, j, player):
                    moves.append((i, j))
        return moves

    # returns false if the move is invalid and if valid updates the board and the scores and returns true
    def make_move(self, x, y, player):
        if not self.validateMove(x, y, player):
            return False

        if player == 0:
            cell = 'w'
        else:
            cell = 'b'

        self.update_board(x, y, player)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            resx = -1
            resy = -1
            for j in range(9):
                newx = x + dx[i] * j
                newy = y + dy[i] * j
                if newx <= 0 or newy <= 0 or newx > 8 or newy > 8 or self.board[newx - 1][newy - 1] == '.':
                    break
                if self.board[newx - 1][newy - 1] == cell:
                    resx = newx
                    resy = newy
            if resx != -1:
                for j in range(9):
                    newx = x + dx[i] * j
                    newy = y + dy[i] * j
                    if newx == resx and newy == resy:
                        break
                    self.update_board(newx, newy, player)

        return True

    # returns false if the move is invalid and true if it's valid
    def validateMove(self, x, y, player):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        check = [False, False, False, False]
        if x <= 0 or y <= 0 or x > 8 or y > 8 or self.board[x - 1][y - 1] != '.':
            return False
        if player == 0:
            cell = 'w'
        else:
            cell = 'b'
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx <= 0 or newy <= 0 or newx > 8 or newy > 8:
                continue
            if self.board[newx - 1][newy - 1] != '.' and self.board[newx - 1][newy - 1] != cell:
                check[i] = True
        validMove = False
        for i in range(4):
            if not check[i]:
                continue
            found = False
            for j in range(1, 9):
                newx = x + dx[i] * j
                newy = y + dy[i] * j
                if newx <= 0 or newy <= 0 or newx > 8 or newy > 8 or self.board[newx - 1][newy - 1] == '.':
                    break
                if self.board[newx - 1][newy - 1] == cell:
                    found = True
            if found:
                validMove = True
        return validMove

    # updates a cell of the board and changes the score of the players
    def update_board(self, x, y, player):
        if player == 0:
            cell = 'w'
        else:
            cell = 'b'
        if self.board[x - 1][y - 1] != cell:
            self.PlayerScores[player] += 1
            if self.board[x - 1][y - 1] != cell and self.board[x - 1][y - 1] != '.':
                self.PlayerScores[(player + 1) % 2] -= 1
        self.board[x - 1][y - 1] = cell

    # prints the board
    def display_board(self):
        for i in range(9):
            print(i, end=" ")
        print()
        for i in range(8):
            print(i + 1, end=" ")
            for element in self.board[i]:
                print(element, end=" ")
            print()
        print()

    def player_vs_player(self):
        while True:
            # Player 1 (black) move
            print("Player 1 (black) turn:")
            self.display_board()
            valid_moves = self.getValidMoves(1)
            print("Valid moves for player 1: ")
            print(valid_moves)
            if not valid_moves:
                print("Player 1 has no valid moves, Skipping turn.")
            else:
                while True:
                    try:
                        x = int(input("Enter row number 1->8: "))
                        y = int(input("Enter column number 1->8: "))
                        if (x, y) in valid_moves:
                            break
                        else:
                            print("Invalid move, try again.")
                    except ValueError:
                        print("Invalid input! please enter integers")
                self.make_move(x, y, 1)

            # Player 2 (white) move
            print("Player 2 (white) turn:")
            self.display_board()
            valid_moves = self.getValidMoves(0)
            print("Valid moves for player 2: ")
            print(valid_moves)
            if not valid_moves:
                print("Player 2 has no valid moves, Skipping turn.")
            else:
                while True:
                    try:
                        x = int(input("Enter row number 1->8: "))
                        y = int(input("Enter column number 1->8: "))
                        if (x, y) in valid_moves:
                            break
                        else:
                            print("Invalid move, try again.")
                    except ValueError:
                        print("Invalid input! please enter integers.")
                self.make_move(x, y, 0)

            # Check if the game is over
            if not self.getValidMoves(0) and not self.getValidMoves(1):
                self.display_board()
                print("Game over!")
                white_score = self.PlayerScores[0]
                black_score = self.PlayerScores[1]
                if white_score == black_score:
                    print("It's a tie!")
                elif white_score > black_score:
                    print("Player 2 (white) wins!")
                else:
                    print("Player 1 (black) wins!")
                break

    def static_evaluation(self, position):
        player_1_score = position.PlayerScores[0]
        player_2_score = position.PlayerScores[1]
        return player_1_score - player_2_score

    def get_children(self, position):
        children = []
        for i in range(1, 9):
            for j in range(1, 9):
                if position.validateMove(i, j, 0):
                    child_position = Controller()
                    child_position.board = [row[:] for row in position.board]
                    child_position.PlayerScores = position.PlayerScores[:]

                    child_position.make_move(i, j, 0)

                    children.append(child_position)
        return children

    def minimax(self, position, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or (not position.getValidMoves(0) and not position.getValidMoves(1)):
            return self.static_evaluation(position), None

        if maximizingPlayer:
            maxEval = float('-inf')
            best_move = None
            for child in self.get_children(position):
                eval, _ = self.minimax(child, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                if eval == maxEval:
                    best_move = child
            return maxEval, best_move
        else:
            minEval = float('inf')
            best_move = None
            for child in self.get_children(position):
                eval, _ = self.minimax(child, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
                if eval == minEval:
                    best_move = child
            return minEval, best_move


    def player_vs_computer(self):
        # Get depth from user
        depth = self.get_depth()

        while True:
            # Player (black) move
            print("Player (black) turn:")
            self.display_board()
            valid_moves = self.getValidMoves(1)
            print("Valid moves for player: ", valid_moves)
            if not valid_moves:
                print("Player has no valid moves, Skipping turn.")
            elif self.getValidMoves(0) and not self.getValidMoves(1):
                print("will enter infinte lop")
                white_score = self.PlayerScores[0]
                black_score = self.PlayerScores[1]
                if white_score == black_score:
                    print("It's a tie!")
                elif white_score > black_score:
                    print("Computer (white) wins!")
                else:
                    print("Player (black) wins!")
                break
            else:
                while True:
                    try:
                        x = int(input("Enter row number 1->8: "))
                        y = int(input("Enter column number 1->8: "))
                        if (x, y) in valid_moves:
                            break
                        else:
                            print("Invalid move, try again.")
                    except ValueError:
                        print("Invalid input! please enter integers")
                self.make_move(x, y, 1)
                self.display_board()

            # Check if the game is over
            if not self.getValidMoves(0) and not self.getValidMoves(1):
                self.display_board()
                print("Game over!")
                white_score = self.PlayerScores[0]
                black_score = self.PlayerScores[1]
                if white_score == black_score:
                    print("It's a tie!")
                elif white_score > black_score:
                    print("Computer (white) wins!")
                else:
                    print("Player (black) wins!")
                break

            # Computer (white) move
            print("Computer (white) turn:")
            _, best_move = self.minimax(self, depth, float('-inf'), float('inf'), True)
            if best_move:
                self.board = best_move.board
                self.PlayerScores = best_move.PlayerScores
                self.display_board()
            elif self.getValidMoves(0) and not self.getValidMoves(1):
                print("will enter infinte lop")

                white_score = self.PlayerScores[0]
                black_score = self.PlayerScores[1]
                if white_score == black_score:
                    print("It's a tie!")
                elif white_score > black_score:
                    print("Computer (white) wins!")
                else:
                    print("Player (black) wins!")
                break

            else:
                print("Computer has no valid moves, Skipping turn.")

            # Check if the game is over
            if not self.getValidMoves(0) and not self.getValidMoves(1):
                self.display_board()
                print("Game over!")
                white_score = self.PlayerScores[0]
                black_score = self.PlayerScores[1]
                if white_score == black_score:
                    print("It's a tie!")
                elif white_score > black_score:
                    print("Computer (white) wins!")
                else:
                    print("Player (black) wins!")
                break

    def get_depth(self):
        while True:
            try:
                depth = int(input("Enter the desired depth (1 for simple, 3 for moderate, 5 for hard): "))
                if depth in [1, 3, 5]:
                    return depth
                else:
                    print("Invalid depth. Please enter 1, 3, or 5.")
            except ValueError:
                print("Invalid input! please enter an integer.")
