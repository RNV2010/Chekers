import pygame as pg

# windows setting
set_screen = weight, height = 1200, 800
bg_color = (200, 200, 200, 1)


# parametrs init
pg.init()
screen = pg.display.set_mode(set_screen)
screen.fill(bg_color)