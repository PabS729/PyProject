from modules.direction import Direction
from modules.board import Board

left = Direction(-1, 0)
right = Direction(1, 0)
stay = Direction(0, 0)
up = Direction(0, -1)
down = Direction(0, 1)
#the class for playing pacman

class playGame:

    #initializes the game
    def __init__(self, size=10):
        self.size = 0
        while True:
            try:
                self.size = int(input("Please enter a size for the board:"))
                break
            except:
                print("Invalid number, please try again.")

        if self.size < 10 or self.size > 100:
            self.size = size
        self.board = Board(self.size)

    def start_game(self):
        self.board.print_board()
        while True:
            if self.board.is_game_over():
                print("Game Over!")
                return
            self.move_characters()

    def move_characters(self):
        movedir = input("Please enter a direction for movement:")

        if movedir == 'U':
            if self.board.can_move(up):
                self.board.move(up)
                self.board.print_board()
        elif movedir == 'D':
            if self.board.can_move(down):
                self.board.move(down)
                self.board.print_board()
        elif movedir == 'L':
            if self.board.can_move(left):
                self.board.move(left)
                self.board.print_board()
        elif movedir == 'R':
            if self.board.can_move(right):
                self.board.move(right)
                self.board.print_board()
        elif movedir == 'S':
            if self.board.can_move(stay):
                self.board.move(stay)
                self.board.print_board()
        else:
            print("Invalid moves, please try again.")
