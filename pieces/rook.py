from pieces.gamepiece import GamePiece

class Rook(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Rook'
        self.in_start_position = True

    def get_moves(self):
        self.moveset = []
        # until blocked, add all moves on the x- & y-axis, starting from current position
        curr_x = self.current_tile.x
        left_x = curr_x - 1
        right_x = curr_x + 1
        curr_y = self.current_tile.y
        up_y = curr_y + 1
        down_y = curr_y - 1
        print(f'down_y: {down_y}')
        while 9 > left_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(left_x-1, self.current_tile.y-1))
            if success:
                left_x -= 1
            else:
                print(f'here, {left_x-1}, {self.current_tile.y-1}')
                left_x = 0
        while 9 > right_x > 0:
            success = self.add_valid_move(self.gameboard.get_tile(right_x-1, self.current_tile.y-1))

            if success:
                right_x += 1
            else:
                right_x = 9

        while 0 < up_y < 9:
            print(f'here in up_y, {self.current_tile.x - 1}, {up_y - 1}')
            success = self.add_valid_move(self.gameboard.get_tile(self.current_tile.x-1, up_y-1))
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
