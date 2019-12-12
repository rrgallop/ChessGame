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

        self.captures = []

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
            if self.team == 'white':
                self.gameboard.active_team = 'black'
            else:
                self.gameboard.active_team = 'white'
            self.moveset = []
            self.captures = []
        if tile.occupant in self.captures:
            tile.occupant.active = False
            self.current_tile.occupant = None
            tile.occupant = None
            tile.set_occupant(self)
            self.in_start_position = False
            if self.team == 'white':
                self.gameboard.active_team = 'black'
            else:
                self.gameboard.active_team = 'white'
            self.moveset = []
            self.captures = []

    def add_valid_move(self, tile):
        if not tile.is_occupied():
            self.moveset.append(tile)
            return True
        else:
            if self.team is not tile.occupant.team:
                if self.type is not 'Pawn':
                    self.captures.append(tile.occupant)
                # else:
                #     left_tile = self.gameboard.get_tile(self.current_tile.x-2, self.current_tile.y)
                #     right_tile = self.gameboard.get_tile(self.current_tile.x, self.current_tile.y)
                #     if left_tile.is_occupied() and self.team is not left_tile.occupant.team:
                #         self.captures.append(tile.occupant)
                #     if right_tile.is_occupied() and self.team is not right_tile.occupant.team:
                #         self.captures.append(tile.occupant)

            return False

    def within_board(self, tile):
        return 0 <= tile <= 8

    def get_straight_moves(self, king=False):
        curr_x = self.current_tile.x
        left_x = curr_x - 1
        right_x = curr_x + 1
        curr_y = self.current_tile.y
        up_y = curr_y + 1
        down_y = curr_y - 1
        while 9 > left_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(left_x - 1, self.current_tile.y - 1))
            if success and not king:
                left_x -= 1
            else:
                left_x = 0
        while 9 > right_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(right_x - 1, self.current_tile.y - 1))
            if success and not king:
                right_x += 1
            else:
                right_x = 9

        while 0 < up_y < 9:
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, up_y - 1))
            if success and not king:
                up_y += 1
            else:
                up_y = 9

        while 9 > down_y > 0:
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, down_y - 1))
            if success and not king:
                down_y -= 1
            else:
                down_y = 0

    def get_diagonal_moves(self, king=False):
        move_distance = 1
        curr_x = self.current_tile.x - 1
        curr_y = self.current_tile.y - 1
        while 0 <= curr_x + move_distance < 8 and 0 <= curr_y + move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x + move_distance, curr_y + move_distance))
            if success and not king:
                move_distance += 1
            else:
                move_distance = 9
        move_distance = 1
        while 0 <= curr_x + move_distance < 8 and 0 <= curr_y - move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x + move_distance, curr_y - move_distance))
            if success and not king:
                move_distance += 1
            else:
                move_distance = 9
        move_distance = 1
        while 0 <= curr_x - move_distance < 8 and 0 <= curr_y - move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x - move_distance, curr_y - move_distance))
            if success and not king:
                move_distance += 1
            else:
                move_distance = 9
        move_distance = 1
        while 0 <= curr_x - move_distance < 8 and 0 <= curr_y + move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x - move_distance, curr_y + move_distance))
            if success and not king:
                move_distance += 1
            else:
                move_distance = 9

    def __repr__(self):
        """
        toString method
        :return: string representation of GamePiece
        """
        return f"{self.type}, {self.team}, standing on tile {self.current_tile}"