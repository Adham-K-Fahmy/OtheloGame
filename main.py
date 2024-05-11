from Controller import *

if __name__ == '__main__':
    Controller = controller()
    last = 1
    while True:
        if len(Controller.getValidMoves(last)) == 0:
            last = (last + 1) % 2
            continue
        Controller.display_board()
        print("valid moves")
        print(Controller.getValidMoves(last))
        print(Controller.PlayerScores)
        print(f"player {last + 1} turn")
        x = int(input())
        y = int(input())
        if not Controller.make_move(x, y, last):
            print("invalid move")
            continue
        last = (last + 1) % 2