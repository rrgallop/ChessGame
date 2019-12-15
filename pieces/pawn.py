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

        # captures
        if self.within_board(self.current_tile.x-1, self.current_tile.y+direction):
            print(f'left attack: {self.current_tile.x-1},{self.current_tile.y+direction}')
            left_tile = self.gameboard.get_tile(self.current_tile.x-2, self.current_tile.y-1 + direction)

            if left_tile.is_occupied() and self.team != left_tile.occupant.team:
                self.captures.append(left_tile.occupant)

        if self.within_board(self.current_tile.x, self.current_tile.y+direction):
            print(f'right attack: {self.current_tile.x},{self.current_tile.y + direction}')
            right_tile = self.gameboard.get_tile(self.current_tile.x, self.current_tile.y-1 + direction)

            if right_tile.is_occupied() and self.team != right_tile.occupant.team:
                self.captures.append(right_tile.occupant)

        print(f"captures:{self.captures}")




