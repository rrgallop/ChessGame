from board.tile import Tile
from board.board import GameBoard


class GamePiece(object):

    def __init__(self, team):
        self.type = 'Pawn'
        self.team = team
        self.moveset = []
        self.active = True
        self.current_tile = None
        self.team = None

    def __repr__(self):
        return f"{self.type}, {self.team}, standing on tile {self.current_tile}"