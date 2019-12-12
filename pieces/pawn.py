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
        self.captures = []
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
        diag_tile_left = self.gameboard.get_tile(self.current_tile.x - 2, self.current_tile.y - 1 + direction)
        diag_tile_right = self.gameboard.get_tile(self.current_tile.x, self.current_tile.y - 1 + direction)
        self.check_pawn_captures(diag_tile_left, diag_tile_right)
        print(f"captures:{self.captures}")

    def check_pawn_captures(self, lt, rt):
        if lt.is_occupied():
            self.captures.append(lt.occupant)
        if rt.is_occupied():
            self.captures.append(rt.occupant)




