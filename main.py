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
    selected_tile = None
    while run:
        print_board(game.gameboard)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                print("Bye")
            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_tile:
                    selected_tile.selected = False
                    selected_tile = None
                mx, my = pygame.mouse.get_pos()
                tile_x, tile_y = math.floor(mx/SQUARE_SIZE), 7-math.floor(my/SQUARE_SIZE)
                print(f"tile: {tile_x+1},{tile_y+1}")
                selected_tile = game.gameboard.get_tile(tile_x, tile_y)
                print(selected_tile.occupant)
                selected_tile.selected = True


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
    if tile.occupant.team == 'black':
        if tile.occupant.type == 'King':
            screen.blit(black_team[0], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Bishop':
            screen.blit(black_team[1], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Knight':
            screen.blit(black_team[2], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Pawn':
            screen.blit(black_team[3], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Queen':
            screen.blit(black_team[4], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Rook':
            screen.blit(black_team[5], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))

    if tile.occupant.team == 'white':
        if tile.occupant.type == 'King':
            screen.blit(white_team[0], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Bishop':
            screen.blit(white_team[1], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Knight':
            screen.blit(white_team[2], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Pawn':
            screen.blit(white_team[3], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Queen':
            screen.blit(white_team[4], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))
        if tile.occupant.type == 'Rook':
            screen.blit(white_team[5], ((tile.x-1)*SQUARE_SIZE, (8*SQUARE_SIZE)-((tile.y)*SQUARE_SIZE)))


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
                pygame.draw.rect(screen, (0,0,0), ((tile.x-1)*SQUARE_SIZE, ((8*SQUARE_SIZE)-(tile.y)*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, (200,200,200), ((tile.x-1)*SQUARE_SIZE, ((8*SQUARE_SIZE)-(tile.y)*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
            if tile.selected:
                pygame.draw.rect(screen, (200,0,0), ((tile.x-1)*SQUARE_SIZE, ((8*SQUARE_SIZE)-(tile.y)*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE))
            if tile.occupant:
                paint_occupant(tile)

        pygame.display.flip()


screen = pygame.display.set_mode((8*SQUARE_SIZE, 8*SQUARE_SIZE))
screen_title = 'Chess Game'
pygame.display.set_caption(screen_title)
game = Game()
play(game)

