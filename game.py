from modules.direction import Direction
from modules.board import Board

#global directions
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
    
    #starts the game
    def start_game(self):
        self.board.print_board()
        while True:
            if self.board.is_game_over():
                print("Game Over!")
                return
            self.move_characters()

    #moves the pacman and the ghost
    def move_characters(self):
        movedir = input("Please enter a direction for movement:")
        
        #moving up
        if movedir == 'U':
            if self.board.can_move(up):
                self.board.move(up)
                self.board.print_board()
        #moving down
        elif movedir == 'D':
            if self.board.can_move(down):
                self.board.move(down)
                self.board.print_board()
        #moving left
        elif movedir == 'L':
            if self.board.can_move(left):
                self.board.move(left)
                self.board.print_board()
        #moving right
        elif movedir == 'R':
            if self.board.can_move(right):
                self.board.move(right)
                self.board.print_board()
        #stay
        elif movedir == 'S':
            if self.board.can_move(stay):
                self.board.move(stay)
                self.board.print_board()
        else:
            print("Invalid moves, please try again.")
