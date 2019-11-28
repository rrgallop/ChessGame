from pieces.gamepiece import GamePiece

class Knight(GamePiece):

    def __init__(self, team):
        self.type = 'Knight'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None