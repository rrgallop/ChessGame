from board.tile import Tile


class GameBoard(object):
    def __init__(self):
        self.tiles = self.generate_tiles()

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

    def __repr__(self):
        return_str = ''
        for x in range(8,0,-1):
            tile_list = self.tiles.get(x)
            for y in range(0,8):
                if tile_list[y].occupant == None:
                    return_str += ' . '
                elif tile_list[y].occupant.type == 'Pawn':
                    return_str += ' P '
                elif tile_list[y].occupant.type == 'King':
                    return_str += ' K '
                elif tile_list[y].occupant.type == 'Queen':
                    return_str += ' Q '
                elif tile_list[y].occupant.type == 'Rook':
                    return_str += ' R '
                elif tile_list[y].occupant.type == 'Knight':
                    return_str += ' k '
                elif tile_list[y].occupant.type == 'Bishop':
                    return_str += ' B '
            return_str += '\n'
        return return_str

