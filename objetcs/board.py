"""Клеточное поле"""


class Board:
    def __init__(self, dimensions):
        # создаем массив с клетками
        self.cells = []
        for i in range(dimensions[0]):
            arr = []
            for j in range(dimensions[1]):
                arr.append(None)
            self.cells.append(arr)
        self.dimensions = dimensions

    def get_cell(self, mouse_pos, cell_size):
        # функция возвращает координаты клетки на поле
        mouse_pos_x = mouse_pos[0]
        mouse_pos_y = mouse_pos[1]
        x = mouse_pos_x // cell_size
        y = mouse_pos_y // cell_size
        return self.cells[x][y]
