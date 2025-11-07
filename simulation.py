from grid import Grid
import pygame

class Simulation:
    def __init__(self, width: int, height: int, cell_size: int):
        self.grid = Grid( width=width, height=height, cell_size=cell_size )
        self.grid.fill_random()
        self.temp_grid = Grid( width=width, height=height, cell_size=cell_size )
        self.rows = height // cell_size
        self.columns = width // cell_size

    def draw(self, window: pygame.Surface):
        self.grid.draw(window)

    def count_live_neighbors(self, grid: Grid, row: int, column: int):
        live_neighbors = 0
        neighbor_offset = [(-1,-1), (-1,0), (-1,1), 
                           (0,-1), (0,1), 
                           (1,-1), (1,0), (1,1)]
        for offset in neighbor_offset:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if grid.cells[new_row][new_column] == 1:
                live_neighbors += 1
        return live_neighbors

    def update(self):
        for row in range(self.rows):
            for column in range(self.columns):
                live_neighbors = self.count_live_neighbors(self.grid, row, column)
                cell_value = self.grid.cells[row][column]
                if cell_value == 1:
                    if live_neighbors > 3 or live_neighbors < 2:
                        self.temp_grid.cells[row][column] = 0
                    else:
                        self.temp_grid.cells[row][column] = 1
                else:
                    if live_neighbors == 3:
                        self.temp_grid.cells[row][column] = 1
                    else:
                        self.temp_grid.cells[row][column] = 0

        for row in range(self.rows):
            for column in range(self.columns):
                self.grid.cells[row][column] = self.temp_grid.cells[row][column]
            