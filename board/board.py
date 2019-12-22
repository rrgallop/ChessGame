from board.tile import Tile


class GameBoard(object):
    def __init__(self, game):

        # tiles range from 1 to 8 in both the x and y planes. they are indexed from 0 to 7 in the game's code
        self.tiles = self.generate_tiles()
        self.in_check = False
        self.active_team = 'white'
        self.game = game

    def get_tile(self, x, y):
        """
        Get tile x,y.

        NOTE: Tiles are organized by row, so all tiles at the same height are
        on the same list. That's why we're doing the [y][x] lookup below.
        :param x: int representing x coord
        :param y: int represeting y coord
        """

        row_tiles = list(self.tiles.values())
        try:
            tile = row_tiles[y][x]
        except IndexError:
            return None
        return tile

    def generate_tiles(self):
        """
        Generates the dictionary of tiles.
        Tiles are organized by row. Tiles on the same row will be stored in the same list.
        Each row therefore has its own list of tiles that are contained within it.
        This is what makes the most sense to me, but hey, it could change later.
        :return: tiles: dictionary of lists of tiles
        """
        tiles = {}
        for y in range(1,9):
            # generate the row of tiles that exist at this height
            tile_list = []
            for x in range(1,9):
                new_tile = Tile(x,y)
                tile_list.append(new_tile)
            tiles[y] = tile_list

        return tiles

    def get_checking_piece(self):
        return self.game.get_checking_piece()

    def __repr__(self):
        """
        ToString method
        :return: string object describing the board
        """
        return_str = ''
        for x in range(8,0,-1):
            tile_list = self.tiles.get(x)
            for y in range(0,8):
                if tile_list[y].occupant == None:
                    return_str += ' . '
                elif tile_list[y].occupant.type == 'Pawn':
                    return_str += ' P ' if tile_list[y].occupant.team == 'white' else ' p '
                elif tile_list[y].occupant.type == 'King':
                    return_str += ' K ' if tile_list[y].occupant.team == 'white' else ' k '
                elif tile_list[y].occupant.type == 'Queen':
                    return_str += ' Q ' if tile_list[y].occupant.team == 'white' else ' q '
                elif tile_list[y].occupant.type == 'Rook':
                    return_str += ' R ' if tile_list[y].occupant.team == 'white' else ' r '
                elif tile_list[y].occupant.type == 'Knight':
                    return_str += ' N ' if tile_list[y].occupant.team == 'white' else ' n '
                elif tile_list[y].occupant.type == 'Bishop':
                    return_str += ' B ' if tile_list[y].occupant.team == 'white' else ' b '
            return_str += '\n'
        return return_str

