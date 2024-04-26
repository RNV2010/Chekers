import pygame as pg
import settings
import modules



b_ch_1 = modules.Checker('black', pos=[250, 50])

x_y_p = modules.draw_chessplate(settings.screen)
print(x_y_p)
while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    b_ch_1.draw(settings.screen)
    pg.display.flip()
