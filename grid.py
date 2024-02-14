import pygame
import random


class Grid: 
    def __init__(self, setting):

        self.rows = setting.rows + 1
        self.cols = setting.cols + 1
        self.cell_size = setting.cell_size
        self.screen = setting.window
        self.colors = setting.Colors

        self.previous_grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.current_grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.setting = setting
        self.current_type = 1
    
    def reset_grid(self):

        self.previous_grid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.current_grid = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def add_cell(self, x, y, value):

        self.current_grid[x][y] = value
    
    def update_grid(self):

        for x in range(self.rows - 1):
            for y in range(self.cols - 1):
                if self.previous_grid[x][y] != 0:
                    self.update_sand(x, y)

    def update_sand(self, x, y):

        if self.previous_grid[x][y+1] == 0:
            self.current_grid[x][y] = 0
            self.current_grid[x][y+1] = 1

        elif self.previous_grid[x-1][y+1] == 0 and self.previous_grid[x+1][y+1] == 0:
            choice = random.randint(0, 1)
            self.current_grid[x][y] = 0

            if choice == 0:
                self.current_grid[x-1][y+1] = 1
            else:
                self.current_grid[x+1][y+1] = 1
        
        elif self.previous_grid[x-1][y+1] == 0:
            self.current_grid[x][y] = 0
            self.current_grid[x-1][y+1] = 1

        elif self.previous_grid[x+1][y+1] == 0:
            self.current_grid[x][y] = 0
            self.current_grid[x+1][y+1] = 1

    def draw_sand(self):
        for x in range(self.rows):
            for y in range(self.cols):
                val = self.current_grid[x][y]
                self.previous_grid[x][y] = val
                pygame.draw.rect(self.screen, self.colors[val], [int(x * self.cell_size), int((y - 1) * self.cell_size), self.cell_size-self.setting.offset, self.cell_size-self.setting.offset])