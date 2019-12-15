import sys, pygame
from board.board import GameBoard
from game import Game
import math

SQUARE_SIZE = 50

BLACK_KING = pygame.image.load('images/black_king.png')
BLACK_QUEEN = pygame.image.load('images/black_queen.png')
BLACK_ROOK = pygame.image.load('images/black_rook.png')
BLACK_BISHOP = pygame.image.load('images/black_bishop.png')
BLACK_KNIGHT = pygame.image.load('images/black_knight.png')
BLACK_PAWN = pygame.image.load('images/black_pawn.png')
black_team = [BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_PAWN, BLACK_QUEEN, BLACK_ROOK]

WHITE_KING = pygame.image.load('images/white_king.png')
WHITE_QUEEN = pygame.image.load('images/white_queen.png')
WHITE_ROOK = pygame.image.load('images/white_rook.png')
WHITE_BISHOP = pygame.image.load('images/white_bishop.png')
WHITE_KNIGHT = pygame.image.load('images/white_knight.png')
WHITE_PAWN = pygame.image.load('images/white_pawn.png')
white_team = [WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_PAWN, WHITE_QUEEN, WHITE_ROOK]


def scale_images(team_list):
    """
    Scales the .png image to fit the current size of the tile.
    :param team_list: A list of pygame image objects, pre-transformation.
    :return: new_team_list: Transformed images are returned in new list object
    """
    new_team_list = []
    for image in team_list:
        new_team_list.append(pygame.transform.scale(image, (50, 50)))
    return new_team_list


white_team = scale_images(white_team)
black_team = scale_images(black_team)


def play(game):
    """
    The main game loop
    :param game: Game object, managing all game data
    :return:
    """
    run = True

    # used by GUI to track the currently selected tile
    selected_tile = None

    # used by GUI to track whether or not a unit is "held" by the mouse cursor
    held_unit = None

    while run:
        mx, my = pygame.mouse.get_pos()
        print_board(game.gameboard)
        if held_unit:
            display_image = get_correct_image(held_unit)
            screen.blit(display_image, (mx, my))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("Bye")

            if event.type == pygame.MOUSEBUTTONUP:
                # release the unit, and if it's released on a tile it can be moved to, move it
                if held_unit:
                    tile_x, tile_y = math.floor(mx / SQUARE_SIZE), 7 - math.floor(my / SQUARE_SIZE)
                    move_tile = game.gameboard.get_tile(tile_x, tile_y)

                    # end turn
                    held_unit.move_to(move_tile)
                    held_unit.on_mouse = False
                    held_unit = None
                    selected_tile.selected = False
                    selected_tile = None



            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_tile:
                    selected_tile.selected = False
                    selected_tile = None
                tile_x, tile_y = math.floor(mx/SQUARE_SIZE), 7-math.floor(my/SQUARE_SIZE)
                print(f"tile: {tile_x+1},{tile_y+1}")
                selected_tile = game.gameboard.get_tile(tile_x, tile_y)
                selected_tile.selected = True

                # code used to "put" selected unit on the mouse cursor
                if selected_tile.is_occupied() and selected_tile.occupant.team == game.gameboard.active_team:
                    print(selected_tile.occupant)
                    held_unit = selected_tile.occupant
                    selected_tile.occupant.on_mouse = True
                    selected_tile.occupant.get_moves()
        pygame.display.flip()


def get_correct_image(gamepiece):
    if gamepiece.team == 'black':
        if gamepiece.type == 'King':
            return black_team[0]
        if gamepiece.type == 'Bishop':
            return black_team[1]
        if gamepiece.type == 'Knight':
            return black_team[2]
        if gamepiece.type == 'Pawn':
            return black_team[3]
        if gamepiece.type == 'Queen':
            return black_team[4]
        if gamepiece.type == 'Rook':
            return black_team[5]
    else:
        if gamepiece.type == 'King':
            return white_team[0]
        if gamepiece.type == 'Bishop':
            return white_team[1]
        if gamepiece.type == 'Knight':
            return white_team[2]
        if gamepiece.type == 'Pawn':
            return white_team[3]
        if gamepiece.type == 'Queen':
            return white_team[4]
        if gamepiece.type == 'Rook':
            return white_team[5]


def paint_occupant(tile):
    """
    Paints the game piece onto the tile that it occupies.

    NOTE: 1,1 in pygame is the top-left corner of the screen.
    1,1 in Chess is the bottom left of the screen.
    If some of the math looks kinda weird at first glance, that's why.
    I'm basically translating between the world of pygame and Chess.

    :param tile: Tile object that we are painting over.
    :return:
    """
    if not tile.occupant.on_mouse:
        display_image = get_correct_image(tile.occupant)
        screen.blit(display_image, ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-(tile.y*SQUARE_SIZE)))


def print_board(board):
    """
    Prints the game board to the screen.

    NOTE: 1,1 in pygame is the top-left corner of the screen.
    1,1 in Chess is the bottom left of the screen.
    If some of the math looks kinda weird at first glance, that's why.
    I'm basically translating between the world of pygame and Chess.

    :param board: The gameboard object
    """
    for k in board.tiles:
        for tile in board.tiles[k]:
            if tile.color == 'black':
                pygame.draw.rect(screen, (0, 0, 0), ((tile.x - 1)*SQUARE_SIZE, (
                        (8 * SQUARE_SIZE) - tile.y*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE
                ))
            else:
                pygame.draw.rect(screen, (200, 200, 200), ((tile.x - 1) * SQUARE_SIZE, (
                        (8*SQUARE_SIZE)-tile.y*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE
                ))
            if tile.selected:
                pygame.draw.rect(screen, (200, 0, 0), ((tile.x - 1) * SQUARE_SIZE, (
                        (8*SQUARE_SIZE)-tile.y*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE
                ))
            if tile.occupant:
                paint_occupant(tile)

                # if the tile has an occupant, and the tile is selected, paint the board to represent
                # the moves currently available to that occupant
                if tile.selected:
                    for move in tile.occupant.moveset:
                        pygame.draw.rect(screen, (0, 200, 0), ((move.x - 1) * SQUARE_SIZE, (
                            (8 * SQUARE_SIZE) - move.y * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE
                        ))
                    for capture in tile.occupant.captures:
                        pygame.draw.rect(screen, (100, 100, 0), ((capture.current_tile.x - 1) * SQUARE_SIZE, (
                                (8 * SQUARE_SIZE) - capture.current_tile.y * SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE
                                                               ))
                    pygame.display.flip()


screen = pygame.display.set_mode((8*SQUARE_SIZE, 8*SQUARE_SIZE))
screen_title = 'Chess Game'
pygame.display.set_caption(screen_title)
game = Game()

play(game)

