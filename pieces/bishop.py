from pieces.gamepiece import GamePiece

class Bishop(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Bishop'

    def get_moves(self):
        pass