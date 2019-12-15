from pieces.gamepiece import GamePiece

class Rook(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Rook'
        self.in_start_position = True

    def get_moves(self):
        # until blocked, add all moves on the x- & y-axis, starting from current position
        self.moveset = []
        self.captures = []
        self.get_straight_moves()

