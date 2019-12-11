#the template for pacman and ghosts
class PacCharacter:
    def __init__(self, row, col, appearance):
        self.row = row
        self.col = col
        self.appearance = appearance

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_appearance(self):
        return self.appearance

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def set_appearance(self, appearance):
        self.appearance = appearance