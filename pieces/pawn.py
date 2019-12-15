from board.tile import Tile
from board.board import GameBoard
from pieces.gamepiece import GamePiece


class Pawn(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Pawn'
        self.in_start_position = True
        self.enpassant_possible = 0
        self.direction = 1
        if self.team == 'black':
            self.direction = -1

    def move_to(self, tile):
        if tile in self.moveset:
            self.current_tile.occupant = None

            if self.in_start_position and tile.y == self.current_tile.y+(self.direction*2):
                self.in_start_position = False
                self.enpassant_possible = 2
            else:
                if self.in_start_position and not tile.y == self.current_tile.y+(self.direction*2):
                    self.in_start_position = False
            tile.set_occupant(self)

        if tile in self.captures:
            if tile.is_occupied():
                tile.occupant.active = False
                self.current_tile.occupant = None
                tile.occupant = None
                tile.set_occupant(self)
            else:
                occupied_tile = self.gameboard.get_tile(tile.x-1, tile.y-1-self.direction)
                print(occupied_tile.occupant)
                occupied_tile.occupant.active = False
                self.current_tile.occupant = None
                occupied_tile.occupant = None
                tile.set_occupant(self)

    def get_moves(self):
        self.moveset = []
        self.captures = []

        if self.in_start_position:
            self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + self.direction))
            if not self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + self.direction).is_occupied():
                self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + self.direction*2))
        else:
            if 1 < self.current_tile.y < 8:
                self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, self.current_tile.y - 1 + self.direction))

        # diagonal left capture
        if self.within_board(self.current_tile.x-1, self.current_tile.y+self.direction):
            diag_left_tile = self.gameboard.get_tile(self.current_tile.x-2, self.current_tile.y-1 + self.direction)
            if diag_left_tile.is_occupied() and self.team != diag_left_tile.occupant.team:
                if not self.gameboard.in_check:
                    self.captures.append(diag_left_tile)
                    if diag_left_tile.occupant.type == 'King':
                        self.gameboard.in_check = True
                        self.is_checking = True
                else:
                    if diag_left_tile.occupant.is_checking:
                        self.captures.append(diag_left_tile)

            # en passant
            left_tile = self.gameboard.get_tile(self.current_tile.x - 2, self.current_tile.y - 1)
            if left_tile.is_occupied():
                if left_tile.occupant.type == 'Pawn':
                    if self.team != left_tile.occupant.team and left_tile.occupant.enpassant_possible:
                        self.captures.append(diag_left_tile)

        # diagonal right capture
        if self.within_board(self.current_tile.x, self.current_tile.y+self.direction):
            diag_right_tile = self.gameboard.get_tile(self.current_tile.x, self.current_tile.y-1 + self.direction)
            if diag_right_tile.is_occupied() and self.team != diag_right_tile.occupant.team:
                if not self.gameboard.in_check:
                    self.captures.append(diag_right_tile)
                else:
                    if diag_right_tile.occupant.is_checking:
                        self.captures.append(diag_right_tile)

            # en passant
            right_tile = self.gameboard.get_tile(self.current_tile.x, self.current_tile.y-1)
            if right_tile.is_occupied():
                if right_tile.occupant.type == 'Pawn':
                    if self.team != right_tile.occupant.team and right_tile.occupant.enpassant_possible:
                        self.captures.append(diag_right_tile)



