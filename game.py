from board.board import GameBoard
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.king import King
from pieces.queen import Queen


class Game(object):
    def __init__(self):
        self.gameboard = GameBoard(self)
        self.black_team = self.generate_black_team()
        self.white_team = self.generate_white_team()
        self.black_king = None
        self.white_king = None

    def get_checking_piece(self):
        for piece in self.white_team:
            if piece.is_checking:
                return piece

        for piece in self.black_team:
            if piece.is_checking:
                return piece

    def get_white_moves(self):
        for piece in self.white_team:
            if piece.active:
                piece.get_moves()
                if piece.type == 'Pawn' and piece.enpassant_possible:
                        piece.enpassant_possible -= 1

    def get_black_moves(self):
        for piece in self.black_team:
            if piece.active:
                piece.get_moves()
                if piece.type == 'Pawn' and piece.enpassant_possible:
                    piece.enpassant_possible -= 1

    def get_moves(self):
        self.get_white_moves()
        self.get_black_moves()

    def end_turn(self):
        self.get_moves()
        if self.gameboard.active_team == 'white':
            self.gameboard.active_team = 'black'
        else:
            self.gameboard.active_team = 'white'
        print(f'check: {self.gameboard.in_check}')

    def generate_black_team(self):
        pawn_row = self.gameboard.tiles[7]
        team = 'black'
        team_roster = []
        for _ in range(0, len(pawn_row)):
            this_tile = pawn_row[_]
            new_piece = Pawn(team, self.gameboard, this_tile)
            team_roster.append(new_piece)

        back_row_roster = self.generate_back_row(team)
        for piece in back_row_roster:
            team_roster.append(piece)

        return team_roster

    def generate_white_team(self):
        pawn_row = self.gameboard.tiles[2]
        team = 'white'
        team_roster = []
        for _ in range(0, len(pawn_row)):
            this_tile = pawn_row[_]
            new_piece = Pawn(team, self.gameboard, this_tile)
            team_roster.append(new_piece)

        back_row_roster = self.generate_back_row(team)
        for piece in back_row_roster:
            team_roster.append(piece)

        return team_roster

    def generate_back_row(self, team):
        """
        Generates the game pieces on the back row of the team.
        Because the row positions are identical for both teams, they can
        be generated by the same method.
        :return: a list of GamePiece objects
        """
        if team == 'black':
            back_row = self.gameboard.tiles[8]
        else:
            back_row = self.gameboard.tiles[1]

        back_row_roster = []
        left_rook = Rook(team, self.gameboard, back_row[0])
        left_knight = Knight(team, self.gameboard, back_row[1])
        left_bishop = Bishop(team, self.gameboard, back_row[2])
        king = King(team, self.gameboard, back_row[3])
        queen = Queen(team, self.gameboard, back_row[4])
        right_bishop = Bishop(team, self.gameboard, back_row[5])
        right_knight = Knight(team, self.gameboard, back_row[6])
        right_rook = Rook(team, self.gameboard, back_row[7])

        back_row_roster.append(left_rook)
        back_row_roster.append(left_knight)
        back_row_roster.append(left_bishop)
        back_row_roster.append(queen)
        back_row_roster.append(king)
        back_row_roster.append(right_bishop)
        back_row_roster.append(right_knight)
        back_row_roster.append(right_rook)

        if team is 'black':
            self.black_king = king
        elif team is 'white':
            self.white_king = king

        return back_row_roster
