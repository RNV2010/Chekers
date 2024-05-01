import pygame as pg
import settings
import modules



b_ch_1 = modules.Checker('black', pos=[250, 50])

x_y_p = modules.draw_chessplate(settings.screen)
print(x_y_p)
while True:
    settings.screen.fill(settings.bg_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if modules.check_collision(event.pos, b_ch_1.get_pos(), radius=40):
                    b_ch_1.dragging(True)
                    temp_ch_pos = b_ch_1.get_pos()
                    b_ch_1.set_offset([temp_ch_pos[0] - event.pos[0], temp_ch_pos[1] - event.pos[0]])
        elif event.type == pg.MOUSEBUTTONUP:
            if b_ch_1._drag:
                b_ch_1.dragging(False)
                b_ch_1.set_pos([b_ch_1._offset[0] + event.pos[0], b_ch_1._offset[1] + event.pos[0]])
        elif event.type == pg.MOUSEMOTION:
            if b_ch_1._drag:
                b_ch_1.set_pos([b_ch_1._offset[0] + event.pos[0], b_ch_1._offset[1] + event.pos[0]])
    b_ch_1.draw(settings.screen)
    pg.display.flip()
