from PygameSetUp import pg
from Enums import Color


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.player_points = 0

    def draw_symbol(self):
        pg.draw.circle(self.screen.game_window, Color.RED.value, pg.mouse.get_pos(), 10)

    def set_player_points(self, point: int):
        self.player_points += point

    def get_player_points(self) -> int:
        return self.player_points
