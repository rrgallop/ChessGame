from board.board import GameBoard
from pieces.pawn import Pawn
from pieces.bishop import Bishop


class Game(object):
    def __init__(self):
        self.gameboard = GameBoard()
        self.black_team = self.generate_black_team()
        self.white_team = self.generate_white_team()

    def generate_black_team(self):
        team_row = self.gameboard.tiles[7]
        team = 'black'
        team_roster = []
        for _ in range(0, len(team_row)):
            this_tile = team_row[_]
            new_piece = Pawn(team)
            this_tile.set_occupant(new_piece)
            team_roster.append(new_piece)
        print(team_roster)
        return team_roster

    def generate_white_team(self):
        return 2
