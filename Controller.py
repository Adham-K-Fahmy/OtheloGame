class controller:
    # player 0 is white
    # player 1 is black
    # the indices used are one-based
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'w', 'b', '.', '.', '.'],
             ['.', '.', '.', 'b', 'w', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]
    PlayerScores = [2, 2]

    def __init__(self):
        pass

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
        dx = [0, 0, 1, -1, 1, -1, 1, -1]
        dy = [1, -1, 0, 0, 1, -1, -1, 1]
        for i in range(8):
            resx = -1
            resy = -1
            for j in range(9):
                newx = x + dx[i] * j
                newy = y + dy[i] * j
                if newx <= 0 or newy <= 0 or newx > 8 or newy > 8 or self.board[newx-1][newy-1] == '.':
                    break
                if self.board[newx-1][newy-1] == cell:
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
        dx = [0, 0, 1, -1, 1, -1, 1, -1]
        dy = [1, -1, 0, 0, 1, -1, -1, 1]
        if x <= 0 or y <= 0 or x > 8 or y > 8 or self.board[x - 1][y - 1] != '.':
            return False
        if player == 0:
            cell = 'w'
        else:
            cell = 'b'
        validMove = False
        for i in range(8):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx <= 0 or newy <= 0 or newx > 8 or newy > 8:
                continue
            if self.board[newx - 1][newy - 1] != '.' and self.board[newx - 1][newy - 1] != cell:
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
