from PygameSetUp import pg
from Enums import Color


class Player1:
    def __init__(self, screen):
        self.screen = screen
        self.player_points = 0

    def draw_symbol(self):
        pg.draw.circle(self.screen.game_window, Color.RED.value, pg.mouse.get_pos(), 45)
        pg.draw.circle(self.screen.game_window, Color.BG.value, pg.mouse.get_pos(), 35)

    def set_player_points(self, point: int):
        self.player_points += point

    def get_player_points(self) -> int:
        return self.player_points


class Player2:
    def __init__(self, screen):
        self.screen = screen
        self.player_points = 0
