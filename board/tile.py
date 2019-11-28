class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupant = None
        self.color = self.assign_color()

    def set_occupant(self, gamepiece):
        self.occupant = gamepiece
        gamepiece.current_tile = self

    def assign_color(self):
        row_starts_with_white = True
        if self.y % 2 == 0:
            row_starts_with_white = False
        if row_starts_with_white:
            if self.x % 2 == 1:
                return 'white'
            else:
                return 'black'
        else:
            if self.x % 2 == 1:
                return 'black'
            else:
                return 'white'

    def __str__(self):
        return str(self.x)+','+str(self.y)

    def __repr__(self):
        return str(self.x)+','+str(self.y)+' c: '+str(self.color)
