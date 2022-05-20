"""Город"""


from objetcs.cells.cell import Cell
from imagelib.load import load_image
import random


images = ["town1.png", "town2.png"]


class TownCell(Cell):

    def __init__(self, board, size, coords, *group):
        img = random.choice(images)
        self.image = load_image(img, (size, size))
        name = "Town"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass