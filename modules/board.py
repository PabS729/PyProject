from .direction import Direction
from .pac_character import PacCharacter

left = Direction(-1, 0)
right = Direction(1, 0)
stay = Direction(0, 0)
up = Direction(0, -1)
down = Direction(0, 1)

#the board for playing the game
class Board:
    
    #pacman initializes at the middle of the grid
    #ghosts initializes at the four corners of the grid
    def __init__(self, size=10):
        self.GRID_SIZE = size;
        self.grid = []
        self.visited = []

        for i in range(0, size):
            self.grid.append([])
            for index in range(0, size):
                self.grid[i].append(' ')

        for i in range(0, size):
            self.visited.append([])
            for index in range(0, size):
                self.visited[i].append(False)
        self.score = 0;

        self.pacman = PacCharacter(int(size / 2), int(size / 2), 'P');
        self.ghosts = [PacCharacter] * 4;
        self.ghosts[0] = PacCharacter(0, 0, 'G');
        self.ghosts[1] = PacCharacter(0, size - 1, 'G');
        self.ghosts[2] = PacCharacter(size - 1, 0, 'G');
        self.ghosts[3] = PacCharacter(size - 1, size - 1, 'G');

        self.set_visited(int(self.GRID_SIZE / 2), int(self.GRID_SIZE / 2));

        self.refresh_grid();

    def get_score(self):
        return self.score

    def get_grid(self):
        return self.grid
    
    #set the cell to be visited if the pacman has been to the cell before
    def set_visited(self, x, y):
        if x < 0 or y < 0 or x > self.GRID_SIZE or y > self.GRID_SIZE:
            return
        self.visited[x][y] = True

    #updates the status of the board
    def refresh_grid(self):

        for i in range(0, self.GRID_SIZE):
            for j in range(0, self.GRID_SIZE):
                if not self.visited[i][j]:
                    self.grid[i][j] = '*'
                else:
                    self.grid[i][j] = ' '

        self.grid[self.pacman.get_row()][self.pacman.get_col()] = \
            self.pacman.get_appearance()
        for ghost in self.ghosts:
            if self.pacman.get_row() == ghost.get_row() and \
                    self.pacman.get_col() == ghost.get_col():
                self.grid[ghost.get_row()][ghost.get_col()] = 'X';
            else:
                self.grid[ghost.get_row()][ghost.get_col()] = \
                    ghost.get_appearance();

    #check if the pacman can move in a certain direction
    def can_move(self, direction):
        if direction == None:
            return False

        pacmanRow = self.pacman.get_row() + direction.get_y()
        pacmanCol = self.pacman.get_col() + direction.get_x()

        return pacmanRow >= 0 and pacmanRow < self.GRID_SIZE and \
               pacmanCol >= 0 and pacmanCol < self.GRID_SIZE

    #moves the pacman and the ghosts
    def move(self, direction):
        pacmanRow = self.pacman.get_row() + direction.get_y()
        pacmanCol = self.pacman.get_col() + direction.get_x()

        self.pacman.set_position(pacmanRow, pacmanCol)

        if not self.visited[pacmanRow][pacmanCol]:
            self.score += 10
            self.set_visited(pacmanRow, pacmanCol)

        for ghost in self.ghosts:
            self.ghost_move(ghost)

        self.refresh_grid()

    #check if the game is over
    def is_game_over(self):
        pacmanRow = self.pacman.get_row();
        pacmanCol = self.pacman.get_col();
        for ghost in self.ghosts:
            if ghost.get_row() == pacmanRow and ghost.get_col() == pacmanCol:
                return True
        return False

    #algorithm for moving the ghost
    def ghost_move(self, ghost):
        pacmanRow = self.pacman.get_row();
        pacmanCol = self.pacman.get_col();

        ghostRow = ghost.get_row()
        ghostCol = ghost.get_col()

        rowDist = abs(ghostRow - pacmanRow)
        colDist = abs(ghostCol - pacmanCol)

        if rowDist == 0 and colDist > 0:
            if ghostCol - pacmanCol > 0:
                ghost.set_position(ghostRow, ghostCol - 1);
                return left
            else:  # ghostCol - pacmanCol < 0
                ghost.set_position(ghostRow, ghostCol + 1);
                return right
        elif rowDist > 0 and colDist == 0:
            if ghostRow - pacmanRow > 0:
                ghost.set_position(ghostRow - 1, ghostCol);
                return up;
            else:  # ghostRow - pacmanRow < 0
                ghost.set_position(ghostRow + 1, ghostCol);
                return down;
        elif rowDist == 0 and colDist == 0:
            return stay;

        else:
            if rowDist < colDist:
                if ghostRow - pacmanRow > 0:
                    ghost.set_position(ghostRow - 1, ghostCol);
                    return up;
                else:  # ghostRow - pacmanRow < 0
                    ghost.set_position(ghostRow + 1, ghostCol);
                    return down;
            else:
                if ghostCol - pacmanCol > 0:
                    ghost.set_position(ghostRow, ghostCol - 1);
                    return left;
                else:  # ghostCol - pacmanCol < 0
                    ghost.set_position(ghostRow, ghostCol + 1);
                    return right;

    #prints the board on the terminal
    def print_board(self):
        print("score: " + str(self.score) + '\n')
        for lines in self.grid:
            for char in lines:
                print('  ' + char, end = '')
            print('\n')