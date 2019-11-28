from pieces.gamepiece import GamePiece

class King(GamePiece):

    def __init__(self, team):
        self.type = 'King'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None