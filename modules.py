import pygame as pg


class Checker:
    def __init__(self, team: str, pos: list[float, float], queen: bool = False, size: int = 80):
        self.__team = team
        self.__queen = queen
        self.__pos = pos
        self.__radius = size / 2
        self._drag = False
        self._offset = [0, 0]

    def set_offset(self, pos: list[float, float]) -> None:
        self._offset = pos

    def get_pos(self) -> list:
        return self.__pos

    def set_pos(self, pos: list[float, float]) -> None:
        self.__pos = pos

    def dragging(self, status: bool) -> None:
        self._drag = status

    def draw(self, screen) -> None:
        w_color = (235, 235, 235)
        r_color = (180, 10, 10)
        g_color = (150, 150, 150)
        b_color = (30, 30, 30)
        if self.__team == 'white':
            pg.draw.circle(screen, b_color, self.__pos, self.__radius)
            pg.draw.circle(screen, w_color, self.__pos, self.__radius - 1)
            pg.draw.circle(screen, g_color, self.__pos, self.__radius - 7)
            pg.draw.circle(screen, w_color, self.__pos, self.__radius - 9)
            pg.draw.circle(screen, g_color, self.__pos, self.__radius - 17)
            pg.draw.circle(screen, w_color, self.__pos, self.__radius - 19)
        elif self.__team == 'black':
            pg.draw.circle(screen, b_color, self.__pos, self.__radius)
            pg.draw.circle(screen, r_color, self.__pos, self.__radius - 1)
            pg.draw.circle(screen, b_color, self.__pos, self.__radius - 7)
            pg.draw.circle(screen, r_color, self.__pos, self.__radius - 9)
            pg.draw.circle(screen, b_color, self.__pos, self.__radius - 17)
            pg.draw.circle(screen, r_color, self.__pos, self.__radius - 19)
        else:
            pass


# Draw chessplate
def draw_rect(screen, start_pos=(0, 0), length_d_r=(50, 50), step_pos=(0, 0), num_repeat=1, color=(0, 0, 0)):
    pos = start_pos
    for i in range(num_repeat):
        if i == 0:
            pg.draw.rect(screen, color, (pos[0], pos[1], length_d_r[0], length_d_r[1]))
            continue
        pos[0] += step_pos[0]
        pos[1] += step_pos[1]
        pg.draw.rect(screen, color, (pos[0], pos[1], length_d_r[0], length_d_r[1]))


def draw_chessplate(screen, num_rect=4, num_row=8):
    window_size = pg.display.get_window_size()
    y_out = y_start_pos = window_size[1] / 2 - 4 * 100
    x_out = x_start_pos = window_size[0] / 2 - 4 * 100
    # right_repeat = 4
    for i in range(num_row):
        if i == 0:
            draw_rect(screen, [x_start_pos, y_start_pos], [100, 100], [200, 0], num_rect)
            continue
        y_start_pos += 100

        if i % 2 == 0:
            draw_rect(screen, [x_start_pos, y_start_pos], [100, 100], [200, 0], num_rect)
        else:
            draw_rect(screen, [x_start_pos + 100, y_start_pos], [100, 100], [200, 0], num_rect)

    return x_out, y_out


def new_game() -> object:
    pass


def check_collision(pos1: list[float, float], pos2: list[float, float], radius: int) -> bool:
    dist = ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5
    return dist <= radius * 2


