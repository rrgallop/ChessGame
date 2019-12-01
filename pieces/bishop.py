from pieces.gamepiece import GamePiece

class Bishop(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Bishop'

    def get_moves(self):
        """
        Bishop moves:
            Diagonal rays in the +x,+y, +x,-y, -x,+y, -x,-y directions until blocked
        :return:
        """
        self.moveset = []
        self.get_diagonal_moves()
        print(f"moves:{self.moveset}")
