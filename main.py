import pygame
from objetcs.cells.field import FieldCell
from objetcs.cells.farm import FarmCell
from objetcs.cells.forest import ForestCell
from objetcs.cells.water import WaterCell
from objetcs.cells.mountain import MountainCell
from objetcs.cells.town import TownCell
from objetcs.board import Board
import random


CELL_SIZE = 100
BOARD_DIMENSIONS = (17, 9)
RANDOM_ARRAY = ["field", "field", "field", "field", "field", "field",
                "field", "field", "field", "field", "field", "field",
                "forest", "forest", "forest", "forest", "forest", "forest",
                "farm",
                "water", "water",
                "town",
                "mountain"]


if __name__ == '__main__':
    gameboard = Board(BOARD_DIMENSIONS)

    pygame.init()
    size = (BOARD_DIMENSIONS[0] * CELL_SIZE, BOARD_DIMENSIONS[1] * CELL_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()
    for y in range(BOARD_DIMENSIONS[1]):
        for x in range(BOARD_DIMENSIONS[0]):
            obj = random.choice(RANDOM_ARRAY)
            if obj == "field":
                FieldCell(gameboard, CELL_SIZE, (x, y), all_sprites)
            elif obj == "forest":
                ForestCell(gameboard, CELL_SIZE, (x, y), all_sprites)
            elif obj == "farm":
                FarmCell(gameboard, CELL_SIZE, (x, y), all_sprites)
            elif obj == "water":
                WaterCell(gameboard, CELL_SIZE, (x, y), all_sprites)
            elif obj == "mountain":
                MountainCell(gameboard, CELL_SIZE, (x, y), all_sprites)
            elif obj == "town":
                TownCell(gameboard, CELL_SIZE, (x, y), all_sprites)

    running = True
    while running:
        all_sprites.draw(screen)
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    print(gameboard.get_cell(event.pos, CELL_SIZE))
        pygame.display.flip()
    pygame.quit()