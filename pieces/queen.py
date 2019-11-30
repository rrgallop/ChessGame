from pieces.gamepiece import GamePiece


class Queen(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Queen'

    def get_moves(self):
        pass
