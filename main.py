import pygame as pg
import settings
import modules



w_ch_1 = modules.Checker('white', pos=[250, 50])


while True:
    modules.draw_chessplate(settings.screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    w_ch_1.draw(settings.screen)
    pg.display.flip()
