from board.tile import Tile
from board.board import GameBoard
from pieces.gamepiece import GamePiece

class Pawn(GamePiece):

    def __init__(self, team):
        self.type = 'Pawn'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None
        self.in_start_position = True

    def get_moves(self):
        """
        Generates the set of tiles that are available for the piece to move to
        next turn. team_factor is used to control direction of advancement on y-axis.
        :return:
        """
        available_moves = []
        if self.team == 'black':
            team_factor = -1
        elif self.team == 'white':
            team_factor = 1

        # if self.in_start_position:
            


