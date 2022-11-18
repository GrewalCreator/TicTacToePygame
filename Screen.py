from PygameSetUp import pg

from Enums import Color


class Screen:
    def __init__(self):
        # Init Window Size Values
        self.w_size_x: int = 720
        self.w_size_y: int = 420
        self.game_window = pg.display.set_mode((self.w_size_x, self.w_size_y), pg.RESIZABLE)

    def screen_setup(self):
        board = Board(self.w_size_x, self.w_size_y, self.game_window)
        pg.display.set_caption("Tic Tac Toe")

        # Set Background
        self.game_window.fill(Color.BG.value)
        board.draw_board()

        pg.display.update()


class Board:
    def __init__(self, width, height, game_window):
        self.screen = Screen()
        self.width = width
        self.height = height
        self.game_window = game_window

    def draw_board(self):
        # Rect = (Screen, Color, (x,y,width,height))

        # Left Vertical
        pg.draw.rect(self.game_window, Color.LINE.value, pg.Rect((self.width // 4), 50, 5, self.height - 100))

        # Right Vertical
        pg.draw.rect(self.game_window, Color.LINE.value, pg.Rect(((self.width * 2) // 5), 50, 5, self.height - 100))

        # Top Horizontal
        pg.draw.rect(self.game_window, Color.LINE.value, pg.Rect(75, self.width // 4 - 25, self.height - 100, 5))

        # Bottom Horizontal
        pg.draw.rect(self.game_window, Color.LINE.value, pg.Rect(75, self.width * 2 // 5 - 25, self.height - 100, 5))

        # Square Outline
        pg.draw.rect(self.game_window, Color.BLACK.value, pg.Rect((self.width // 9) - 5, 50, 325, 325), 5)
