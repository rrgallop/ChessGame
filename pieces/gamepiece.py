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
        cpiece = self.gameboard.get_checking_piece()
        true_occupant = tile.occupant
        tile.occupant = self
        cpiece.get_moves()
        saves_king = True
        for piece in cpiece.captures:
            if piece.occupant.type == 'King':
                saves_king = False
        tile.occupant = true_occupant
        return saves_king

    def get_other_team(self):
        if self.team is 'white':
            return self.gameboard.game.black_team
        else:
            return self.gameboard.game.white_team

    def move_is_safe(self, tile):
        if self.type is not 'King':
            return True
        if self.type is 'King':
            # true_occupant = tile.occupant
            # tile.occupant = self
            # if self.team == 'white':
            #     self.gameboard.game.get_black_moves()
            #     team = self.gameboard.game.white_team
            # else:
            #     self.gameboard.game.get_white_moves()
            #     team = self.gameboard.game.black_team
            # for piece in team:
            #     for capture in piece.captures:
            #         if not capture.occupant:
            #             return False
            #         if capture.occupant.type == self.type:
            #             tile.occupant = None
            #             return False
            # tile.occupant = true_occupant
            # return True
            return False

            # other_team = self.get_other_team()
            #
            # for piece in other_team:
            #     if piece.type is not 'Pawn' and piece.active:
            #         for move in piece.moveset:
            #             if piece.type is 'Queen' and piece.active:
            #                 print(f'{self.team} {self.type} is thinking {self.gameboard.get_tile(tile.x-1,tile.y-1)} = {self.gameboard.get_tile(move.x-1,move.y-1)}')
            #             if tile.x == move.x and tile.y == move.y:
            #                 return False
            #     if piece.type is 'Pawn' and piece.active:
            #         if tile.x == piece.current_tile.x+1 and tile.y == piece.current_tile.y+piece.direction:
            #             return False
            #         if tile.x == piece.current_tile.x-1 and tile.y == piece.current_tile.y + piece.direction:
            #             return False
            # return True

    def add_valid_move(self, tile):
        """
        :param tile:
        :return: Boolean used to determine if continued forward movement is possible
        """

        if not self.gameboard.in_check:
            if self.type is 'King' and not tile.is_occupied():
                self.moveset.append(tile)
                return True
            elif self.type is 'King' and self.team is not tile.occupant.team:
                self.add_capture(tile)
                return False
            if self.type is not 'King' and not tile.occupant:
                self.moveset.append(tile)
                return True
            elif self.type is not 'King' and self.team is not tile.occupant.team:
                if self.type is not 'Pawn' and tile.occupant:
                    self.add_capture(tile)
                return False
        #########################################################
        elif self.gameboard.in_check:
            # in check
            if self.is_checking:
                if not tile.occupant:
                    self.moveset.append(tile)
                    return True
                elif self.team is not tile.occupant.team and self.type is not 'Pawn':
                    self.add_capture(tile)
                    return False
            elif not self.is_checking:
                if not tile.occupant and self.gameboard.get_checking_piece().team is not self.team:
                    if self.type is 'King' and not self.intersects_with_check(tile):
                        self.moveset.append(tile)
                        return False
                    if self.type is not 'King' and self.intersects_with_check(tile):
                        self.moveset.append(tile)
                        return False
                    else:  # consider next move but don't append
                        return True
                elif not tile.occupant and self.gameboard.get_checking_piece().team is self.team:
                    self.moveset.append(tile)
            elif self.team is not tile.occupant.team:
                if tile.occupant.is_checking and self.type is not 'Pawn':
                    self.add_capture(tile)
            return False

        return False

    def add_capture(self, tile):
        self.captures.append(tile)
        if tile.occupant.type == 'King':
            # self.gameboard.in_check = True
            self.is_checking = True

    def get_straight_moves(self, king=False):
        curr_x = self.current_tile.x
        left_x = curr_x - 1
        right_x = curr_x + 1
        curr_y = self.current_tile.y
        up_y = curr_y + 1
        down_y = curr_y - 1
        while 9 > left_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(left_x - 1, self.current_tile.y - 1))
            left_x -= 1 if success and not king else 9
        while 9 > right_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(right_x - 1, self.current_tile.y - 1))
            right_x += 1 if success and not king else 9

        while 9 > up_y > 0:
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, up_y - 1))
            up_y += 1 if success and not king else 9

        while 9 > down_y > 0:
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x - 1, down_y - 1))
            down_y -= 1 if success and not king else 9

    def get_diagonal_moves(self, king=False):
        move_distance = 1
        curr_x = self.current_tile.x - 1
        curr_y = self.current_tile.y - 1
        while 0 <= curr_x + move_distance < 8 and 0 <= curr_y + move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x + move_distance, curr_y + move_distance))
            move_distance += 1 if success and not king else 9
        move_distance = 1
        while 0 <= curr_x + move_distance < 8 and 0 <= curr_y - move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x + move_distance, curr_y - move_distance))
            move_distance += 1 if success and not king else 9
        move_distance = 1
        while 0 <= curr_x - move_distance < 8 and 0 <= curr_y - move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x - move_distance, curr_y - move_distance))
            move_distance += 1 if success and not king else 9
        move_distance = 1
        while 0 <= curr_x - move_distance < 8 and 0 <= curr_y + move_distance < 8:
            success = self.add_valid_move(self.gameboard.get_tile(curr_x - move_distance, curr_y + move_distance))
            move_distance += 1 if success and not king else 9

    def __repr__(self):
        """
        toString method
        :return: string representation of GamePiece
        """
        return f"{self.type}, {self.team}, standing on tile {self.current_tile}"
