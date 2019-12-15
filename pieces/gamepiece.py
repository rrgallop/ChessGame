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

        self.is_checking = False

        # the current tile the piece is standing on.
        # only 1 piece can occupy a tile at a time.
        self.current_tile = None
        tile.set_occupant(self)

    def move_to(self, tile):
        if tile in self.moveset:
            self.current_tile.occupant = None
            tile.set_occupant(self)
            self.in_start_position = False
            self.gameboard.in_check = False

        if tile in self.captures:
            tile.occupant.active = False
            self.current_tile.occupant = None
            if tile.occupant.is_checking:
                self.gameboard.in_check = False
                tile.occupant.is_checking = False
            tile.occupant = None
            tile.set_occupant(self)
            self.in_start_position = False

    def intersects_with_check(self, tile):
        checking_piece = self.gameboard.get_checking_piece()
        # print('thinking about ', tile)
        for t in checking_piece.captures:
            if t.occupant.type == 'King':
                king = t.occupant
        for move in checking_piece.moveset:
            # print(f'comparing {tile} to {move}')
            # # if you can intersect a tile in the checking piece's moveset, add that move
            # print(f'{tile.x}={move.x}?  {tile.y}={move.y}?')
            if tile == move:
                # but only if the king is found on the ray of the move
                if self.king_found(tile, checking_piece, king):
                    return True

        return False

    def king_found(self, move, cpiece, king):
        # if the move intersects with the vector of the movement inducing check, it's a valid move
        # print(f'king vector: {king.current_tile.x-cpiece.current_tile.x}, {king.current_tile.y-cpiece.current_tile.y}')
        x_diff = king.current_tile.x-cpiece.current_tile.x
        y_diff = king.current_tile.y-cpiece.current_tile.y

        while x_diff > 0:
            if move.x == cpiece.current_tile.x + x_diff and move.y == cpiece.current_tile.y + y_diff:
                    return True
            x_diff -= 1

        while x_diff < 0:
            if move.x == cpiece.current_tile.x + x_diff and move.y == cpiece.current_tile.y + y_diff:
                    return True
            x_diff += 1

        while y_diff > 0:
            if move.x == cpiece.current_tile.x + x_diff and move.y == cpiece.current_tile.y + y_diff:
                    return True
            y_diff -= 1

        while y_diff < 0:
            if move.x == cpiece.current_tile.x + x_diff and move.y == cpiece.current_tile.y + y_diff:
                    return True
            y_diff += 1
            # print(f'{move.x} == {cpiece.current_tile.x + x_diff} and {move.y} == {cpiece.current_tile.y + y_diff}')

        return False

    def move_is_safe(self, tile):
        if self.type is not 'King':
            return True
        if self.type is 'King':
            if self.team is 'white':
                other_team = self.gameboard.game.black_team
            else:
                other_team = self.gameboard.game.white_team

            for piece in other_team:
                if piece.type is not 'Pawn':
                    for move in piece.moveset:
                        if tile.x == move.x and tile.y == move.y:
                            return False
                if piece.type is 'Pawn':
                    if tile.x == piece.current_tile.x+1 and tile.y == piece.current_tile.y+piece.direction:
                        return False
                    if tile.x == piece.current_tile.x-1 and tile.y == piece.current_tile.y + piece.direction:
                        return False
            return True

    def add_valid_move(self, tile):
        """
        :param tile:
        :return: Boolean used to determine if continued forward movement is possible
        """
        if self.active:
            if not self.gameboard.in_check:
                if self.type is 'King':
                    if not tile.is_occupied():
                        if self.move_is_safe(tile):
                            self.moveset.append(tile)
                        return True
                    else:
                        if self.team is not tile.occupant.team:
                            self.add_capture(tile)
                        return False
                if self.type is not 'King':
                    if not tile.is_occupied():
                        self.moveset.append(tile)
                        return True
                    else:
                        if self.team is not tile.occupant.team:
                            if self.type is not 'Pawn':
                                self.add_capture(tile)
                        return False
            else:
                # in check
                if self.is_checking:
                    if not tile.is_occupied():
                        self.moveset.append(tile)
                        return True
                    else:
                        if self.team is not tile.occupant.team:
                            if self.type is not 'Pawn':
                                self.add_capture(tile)
                        return False
                else:
                    if not self.is_checking:
                        if not tile.is_occupied():

                            if self.type is 'King' and not self.intersects_with_check(tile):
                                    self.moveset.append(tile)

                            if self.intersects_with_check(tile) and self.type is not 'King':
                                    self.moveset.append(tile)
                                    return False
                            else:
                                # consider next move but don't append
                                return True
                        else:
                            if self.team is not tile.occupant.team:
                                if tile.occupant.is_checking:
                                    if self.type is not 'Pawn':
                                        self.add_capture(tile)
                            return False

        return False

    def add_capture(self, tile):
        self.captures.append(tile)
        if tile.occupant.type == 'King':
            self.gameboard.in_check = True
            self.is_checking = True

    def within_board(self, x, y):
        return 0 < x < 8 and 0 < y < 8

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