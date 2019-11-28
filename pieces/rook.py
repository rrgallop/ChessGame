from pieces.gamepiece import GamePiece

class Rook(GamePiece):

    def __init__(self, team):
        self.type = 'Rook'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None