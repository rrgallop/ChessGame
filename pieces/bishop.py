from pieces.gamepiece import GamePiece

class Bishop(GamePiece):

    def __init__(self, team, board):
        super().__init__(team, board)
        self.type = 'Bishop'
