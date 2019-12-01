from pieces.gamepiece import GamePiece

class Knight(GamePiece):

    def __init__(self, team, board, tile):
        super().__init__(team, board, tile)
        self.type = 'Knight'

    def get_moves(self):
        """
        Knight moves: x+2, y+1
                      x+2, y-1
                      x-2, y+1
                      x-2, y-1

                      x+1, y+2
                      x+1, y-2
                      x-1, y+2
                      x-1, y-2
        :return:
        """
        self.moveset = []
        potential_moves = []
        m1x = self.current_tile.x + 2
        m1y = self.current_tile.y + 1
        potential_moves.append(tuple([m1x, m1y]))
        m2x = self.current_tile.x + 2
        m2y = self.current_tile.y - 1
        potential_moves.append(tuple([m2x, m2y]))
        m3x = self.current_tile.x - 2
        m3y = self.current_tile.y + 1
        potential_moves.append(tuple([m3x, m3y]))
        m4x = self.current_tile.x - 2
        m4y = self.current_tile.y - 1
        potential_moves.append(tuple([m4x, m4y]))
        m5x = self.current_tile.x + 1
        m5y = self.current_tile.y + 2
        potential_moves.append(tuple([m5x, m5y]))
        m6x = self.current_tile.x + 1
        m6y = self.current_tile.y - 2
        potential_moves.append(tuple([m6x, m6y]))
        m7x = self.current_tile.x - 1
        m7y = self.current_tile.y + 2
        potential_moves.append(tuple([m7x, m7y]))
        m8x = self.current_tile.x - 1
        m8y = self.current_tile.y - 2
        potential_moves.append(tuple([m8x, m8y]))
        print(f'potential moves: {potential_moves}')
        for move in potential_moves:

            if 0 < move[0] < 9 and 0 < move[1] < 9:
                print(f'in if: {move[0]}, {move[1]}')
                self.add_valid_move(self.gameboard.get_tile(move[0]-1, move[1]-1))

