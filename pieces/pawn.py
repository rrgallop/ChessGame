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

