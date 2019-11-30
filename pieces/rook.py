from pieces.gamepiece import GamePiece

class Rook(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Rook'
        self.in_start_position = True

    def get_moves(self):
        pass