class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

left = Direction(-1, 0)
right = Direction(1, 0)
stay = Direction(0, 0)
up = Direction(0, -1)
down = Direction(0, 1)