from pieces.gamepiece import GamePiece

class King(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'King'

    def get_moves(self):
        self.moveset = []
        self.captures = []
        self.get_diagonal_moves(king=True)
        self.get_straight_moves(king=True)

