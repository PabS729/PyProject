##Pacman in Python

#Game Discription

This is a simplified version of pacman from the original game. In this game, the player controls pacman in a square grid with dots around. When the player moves the pacman around, the pacman eats the pac dots and scores. There are also four ghosts in the game, trying to capture pacman as it moves. 

#How to Start

To start the game, simply open pacman.ipynb in Jupyter Notebook, and run all the cells. 
The player will be prompted to enter a size for the board. The default size is 10. 
There are five choices for the player to move the pacman. Controls are done via the keyboard.
    - U: The pacman moves up one cell.
    - D: The pacman moves down one cell.
    - L: The pacman moves left one cell.
    - R: The pacman moves right one cell.
    - S: The pacman stays at the same spot.
If the player hit other keys, the move will be invalid, and the player has to hit the valid keys again. 

All ghosts will move as the pacman moves. If one of the ghosts capture pacman, the game ends. The player will be prompted to start the game again. Hit "Y" and the game starts again, otherwise, simply hit other keys and the program terminates.
    
#Files:

PyProject/
game.py
    modules/
    board.py:
        pac_character.py
        direction.py            
test.py
pacman.ipynb
tests.ipynb

#File Discription:

pacman.ipynb: The notebook that runs the game
tests.ipynb: The notebook that tests some of the functions from the files

game.py: the main game for pacman.
   - Contains the class playGame

test.py: Unit tests for the classes pacCharacter and Board
   - Contains two methods, test_pacChar() and test_board
   - Tests basic functions such as set_position(), get_row(), get_col(), and move()

modules:
    The modules contain three classes, Board, pacCharacter, Direction. 
    1. board.py:
        - Initializes with given size.
        - Contains the algorithms for moving the pacman and the ghosts. 
        - Refreshes the board after each move. 
    2. pac_character.py:
        - Contains the class pacCharacter.
        - Templates work for both pacman and the ghosts.
    3. direction.py:
        - Templates for left(-1,0), right(1,0), up(0, -1), down(0,1), and stay(0,0)
        - Serve as global directions in the game.
      
