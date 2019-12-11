from modules.pac_character import PacCharacter
from modules.board import Board
from modules.direction import Direction

#Tests pacCharacters
def test_pacChar():

    pacman = PacCharacter(0, 0, 'P')

    assert isinstance(pacman, object)

    p = pacman.get_appearance()
    assert isinstance(p, str)
    assert p == 'P'

    x = pacman.get_row()
    y = pacman.get_col()

    assert isinstance(x, int)
    assert isinstance(y, int)

    assert x == 0
    assert y == 0

    pacman.set_position(3, 4)

    assert pacman.row == 3
    assert pacman.col == 4

    ghost = PacCharacter(1, 2, 'G')

    assert isinstance(ghost, object)

    g = ghost.get_appearance()
    assert isinstance(g, str)
    assert g == 'G'

    x = ghost.get_row()
    y = ghost.get_col()

    assert isinstance(x, int)
    assert isinstance(y, int)

    assert x == 1
    assert y == 2

    ghost.set_position(2, 4)

    assert ghost.row == 2
    assert ghost.col == 4

#Tests the board for the game
def test_board():
    board = Board(15)
    left = Direction(-1, 0)
    right = Direction(1, 0)
    stay = Direction(0, 0)
    up = Direction(0, -1)
    down = Direction(0, 1)

    assert isinstance(board, object)

    assert isinstance(board.GRID_SIZE, int)

    assert board.GRID_SIZE == 15

    assert isinstance(board.pacman, object)
    assert isinstance(board.ghosts, list)

    assert isinstance(board.score, int)

    row = board.pacman.get_row()
    col = board.pacman.get_col()

    board.move(up)

    assert board.score == 10
    assert board.is_game_over() == False
    assert board.pacman.get_row() == row-1
    assert board.pacman.get_col() == col




