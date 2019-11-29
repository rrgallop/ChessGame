from board.tile import Tile
from board.board import GameBoard


class GamePiece(object):

    def __init__(self, team):
        # rook, pawn, king, queen, ...
        self.type = ''

        # black or white
        self.team = team

        # moveset to represent a list of tiles that the piece can potentially move to
        # each piece will have its own method for generating a moveset,
        # called every time the piece lands on a new tile
        # just because a tile is in the moveset doesn't mean the piece can
        # necessarily move to the tile, it will still have to check to
        # make sure the move is valid.
        self.moveset = []

        # a piece is no longer active when it is captured by the opposing team
        self.active = True

        # the current tile the piece is standing on.
        # only 1 piece can occupy a tile at a time.
        self.current_tile = None

    def __repr__(self):
        """
        toString method
        :return: string representation of GamePiece
        """
        return f"{self.type}, {self.team}, standing on tile {self.current_tile}"