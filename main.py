from constants import WINDOW_WIDTH, WINDOW_HEIGHT, DARK_GREY, FPS, CELL_SIZE
import pygame
import sys
from simulation import Simulation

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
simuation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop

while True:

    # 1. Event Handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updating State
    simuation.update()

    # 3. Drawing
    window.fill(DARK_GREY)
    simuation.draw(window)

    pygame.display.update()
    clock.tick(FPS)