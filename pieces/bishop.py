from pieces.gamepiece import GamePiece

class Bishop(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Bishop'

    def get_moves(self):
        self.moveset = []
        curr_x = self.current_tile.x
        left_x = curr_x - 1
        right_x = curr_x + 1
        curr_y = self.current_tile.y
        up_y = curr_y + 1
        down_y = curr_y - 1