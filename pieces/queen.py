from pieces.gamepiece import GamePiece

class Queen(GamePiece):

    def __init__(self, team, board):
        super().__init__(team, board)
        self.type = 'Queen'
        