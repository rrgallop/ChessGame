from pieces.gamepiece import GamePiece

class Bishop(GamePiece):

    def __init__(self, team):
        self.type = 'Bishop'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None