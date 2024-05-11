class controller:
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

    def make_move(self, x, y, player):
        if not self.validateMove(x, y, player):
            return False

        if player == 0:
            cell = 'w'
        else:
            cell = 'b'

        self.update_board(x, y, player)

        for i in range(1, 9):
            if x + i <= 8:
                if self.board[x + i - 1][y - 1] == cell or self.board[x + i - 1][y - 1] == '.':
                    break
                else:
                    self.update_board(x + i, y, player)
        for i in range(1, 9):
            if y + i <= 8:
                if self.board[x - 1][y + i - 1] == cell or self.board[x - 1][y + i - 1] == '.':
                    break
                else:
                    self.update_board(x, y + i, player)

        for i in range(1, 9):
            if x - i > 0:
                if self.board[x - i - 1][y - 1] == cell or self.board[x - i - 1][y - 1] == '.':
                    break
                else:
                    self.update_board(x - i, y, player)
        for i in range(1, 9):
            if y - i > 0:
                if self.board[x - 1][y - i - 1] == cell or self.board[x - 1][y - i - 1] == '.':
                    break
                else:
                    self.update_board(x, y - i, player)
        return True

    def validateMove(self, x, y, player):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        if x <= 0 or y <= 0 or x > 8 or y > 8 or self.board[x - 1][y - 1] != '.':
            print("Invalid Move")
            return False
        if player == 0:
            cell = 'w'
        else:
            cell = 'b'
        validMove = False
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx <= 0 or newy <= 0 or newx > 8 or newy > 8:
                continue
            if self.board[newx - 1][newy - 1] != '.' and self.board[newx - 1][newy - 1] != cell:
                validMove = True
        return validMove

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