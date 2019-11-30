from pieces.gamepiece import GamePiece

class Knight(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Knight'

    def get_moves(self):
        pass
