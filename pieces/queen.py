from pieces.gamepiece import GamePiece


class Queen(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Queen'

    def get_moves(self):
        self.moveset = []
        self.get_straight_moves()
        self.get_diagonal_moves()
        print(f"moves:{self.moveset}")

