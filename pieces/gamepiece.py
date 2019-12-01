from board.tile import Tile
from board.board import GameBoard


class GamePiece(object):

    def __init__(self, team, board, tile):
        # string. 'rook', 'pawn', 'king', 'queen', ...
        self.type = ''

        # 'black' or 'white'
        # ... how about a boolean? to be implemented...
        self.team = team

        # When a piece is clicked on, it will attach to the mouse cursor until
        # the mouse is released. When this happens, we don't want to paint it on the board.
        self.on_mouse = False

        # so the piece can access the gameboard
        self.gameboard = board

        # moveset to represent a list of tiles that the piece can potentially move to
        # each piece will have its own method for generating a moveset,
        # called every time for every active piece every time a piece is moved.
        # only valid moves will make it to the moveset; that is, we will be checking
        # to make sure a move is actually within the bounds of the board, and
        # a path of movement isn't blocked by another piece.
        self.moveset = []

        self.in_start_position = True

        # a piece is no longer active when it is captured by the opposing team
        self.active = True

        # the current tile the piece is standing on.
        # only 1 piece can occupy a tile at a time.
        self.current_tile = None
        tile.set_occupant(self)

    def move_to(self, tile):
        if tile in self.moveset:
            self.current_tile.occupant = None
            tile.set_occupant(self)
            self.in_start_position = False

    def add_valid_move(self, tile):
        if not tile.is_occupied():
            self.moveset.append(tile)
            return True
        else:
            return False

    def get_rook_moves(self):
        curr_x = self.current_tile.x
        left_x = curr_x - 1
        right_x = curr_x + 1
        curr_y = self.current_tile.y
        up_y = curr_y + 1
        down_y = curr_y - 1
        print(f'down_y: {down_y}')
        while 9 > left_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(left_x - 1, self.current_tile.y - 1))
            if success:
                left_x -= 1
            else:
                print(f'here, {left_x - 1}, {self.current_tile.y - 1}')
                left_x = 0
        while 9 > right_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(right_x - 1, self.current_tile.y - 1))

            if success:
                right_x += 1
            else:
                right_x = 9

        while 0 < up_y < 9:
            print(f'here in up_y, {self.current_tile.x - 1}, {up_y - 1}')
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, up_y - 1))
            if success:
                up_y += 1
            else:
                up_y = 9

        while 9 > down_y > 0:
            print(f'here in down_y, {self.current_tile.x - 1}, {down_y - 1}')
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, down_y - 1))
            if success:
                down_y -= 1
            else:
                down_y = 0

    def __repr__(self):
        """
        toString method
        :return: string representation of GamePiece
        """
        return f"{self.type}, {self.team}, standing on tile {self.current_tile}"