from board.tile import Tile
from board.board import GameBoard
from pieces.gamepiece import GamePiece

class Pawn(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Pawn'
        self.in_start_position = True

    def get_moves(self):
        self.moveset = []
        if self.team == 'black':
            direction = -1
        else:
            direction = 1
        if self.in_start_position:
            self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + direction))
            self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + direction*2))
        else:
            self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + direction))
        print(f"moves:{self.moveset}")




