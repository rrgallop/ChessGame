from pieces.gamepiece import GamePiece

class Queen(GamePiece):

    def __init__(self, team):
        self.type = 'Queen'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None