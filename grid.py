import pygame
import random
from constants import GREEN, LIGHT_GREY


class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window: pygame.Surface):
        for row in range(self.rows):
            for column in range(self.columns):
                color = GREEN if self.cells[row][column] else LIGHT_GREY
                rect = ( column * self.cell_size, row * self.cell_size, self.cell_size-1, self.cell_size-1 )
                pygame.draw.rect(window, color, rect)

    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([1,0,0,0])

    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0
    
    def toggle_cell(self, row: int, column: int):
        if 0 <= row <= self.rows and 0 <= column <= self.columns:
            self.cells[row][column] = not self.cells[row][column]