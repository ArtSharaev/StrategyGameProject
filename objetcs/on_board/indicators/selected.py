"""Индикатор выбранной клетки"""


from objetcs.on_board.cell import Cell
from imagelib.load import load_image


class SelectedCell(Cell):

    def __init__(self, board, size, coords, *group):
        self.image = load_image("selected_cell.png", (size, size))
        name = "selected"
        super().__init__(board, size, coords, name, *group)

    def update(self):
        pass