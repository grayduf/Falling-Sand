import pygame
from math import floor
from setting import Setting
from grid import Grid

pygame.init()

setting = Setting()

screen = pygame.display.set_mode(setting.size)
setting.window = screen
clock = pygame.time.Clock()

grid = Grid(setting)

add_cell_radius = 70

update_rate = 0.05
countdown_ms = update_rate
toggle_counter_ms = 0.0
toggle_threshold_ms = 0.125

paused = False
run = True

while run:   
    clock.tick(setting.fps)
    pygame.display.set_caption("Falling Sand - FPS: {}".format(int(clock.get_fps())))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_r:
                grid.reset_grid()

    sec = clock.get_rawtime()/100
    countdown_ms -= sec
    toggle_counter_ms += sec

    if toggle_counter_ms < 0.0:

        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            x_floor = floor(mx/setting.cell_size)
            y_floor = floor(my/setting.cell_size)
            grid.add_cell(x_floor, y_floor, 1)

        if paused == False:
            grid.update_grid()
            countDownMS = update_rate
            grid.draw_sand()

    pygame.display.flip()

pygame.quit()