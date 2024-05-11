from Controller import *

if __name__ == '__main__':
    Controller = controller()
    Controller.display_board()
    Controller.make_move(3, 5, 0)
    Controller.display_board()
    print(Controller.PlayerScores)
    Controller.make_move(3, 4, 1)
    Controller.display_board()
    print(Controller.PlayerScores)