class Tile:
    def __init__(self, x, y):
        # in chess, the X axis is actually represented as a letter of
        # the alphabet, but internally I'm using ints for simplicity
        self.x = x
        self.y = y

        # Tiles can only have one occupant at a time
        self.occupant = None

        # used to track which tile the user has clicked on last
        self.selected = False

        # Tiles are either white or black, so we determine that during board creation
        self.color = self.assign_color()

    def set_occupant(self, gamepiece):
        """
        pretty limited error checking right now, so be expanded later.
        the basic gist here is to set the occupant of the tile and handle all the
        updating necessary, while catching any errors
        :param gamepiece: the new occupant
        :return: True on success, False on failure
        """
        if not self.occupant:
            gamepiece.current_tile = None
            self.occupant = gamepiece
            gamepiece.current_tile = self
            return True
        else:
            print('ERROR TILE ALREADY OCCUPIED')
            return False


    def assign_color(self):
        """
        called during tile creation, just so we know what color the tile should be
        :return: string, 'white' or 'black'
        """
        row_starts_with_white = True
        if self.y % 2 == 0:
            row_starts_with_white = False
        if row_starts_with_white:
            if self.x % 2 == 1:
                return 'black'
            else:
                return 'white'
        else:
            if self.x % 2 == 1:
                return 'white'
            else:
                return 'black'

    def __str__(self):
        return str(self.x)+','+str(self.y)

    def __repr__(self):
        return str(self.x)+','+str(self.y)+' c: '+str(self.color)
