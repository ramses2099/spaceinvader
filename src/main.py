import os
import arcade
from pyglet.image import load as pyglet_load

# SET CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "SPACE INVADER"
PLAYER_SCALING = 0.5
ENEMY_SCALING = 0.8
LASER_SCALING = 0.7
PLAYER_SPEED = 5

# LOAD IMAGES AND ICONS
PATH_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_WINDOWS = os.path.join(PATH_DIR,"images\spaceinvaders.ico")
IMG_PLAYER = os.path.join(PATH_DIR,"images\spaceship.png")
IMG_BACKGROUND = os.path.join(PATH_DIR,"images\\background.jpg")
IMG_ENEMY = os.path.join(PATH_DIR,"images\enemy.png")
IMG_LASER = os.path.join(PATH_DIR,"images\\beam.png")

# CLASS OBJECT
class Player(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(IMG_PLAYER, PLAYER_SCALING)
        self.center_x = (SCREEN_WIDTH / 2) - (self.width / 2)
        self.center_y = y
        self.change_x = 0
        self.life = 3


    def on_update(self, delta_time: float = 1 / 60):
        # self.center_x += self.change_x
        print(f"{self.center_x}")
        #CHECK BOUNDS
        if self.center_x + self.width < 0:
            self.center_x = self.width
            print("ok")
        elif self.center_x + self.width > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH - self.width

class Enemy(arcade.Sprite):
    def __init__(self,x, y):
        super().__init__(IMG_ENEMY, ENEMY_SCALING)
        self.center_x = x
        self.center_y = y

class Bullet(arcade.Sprite):
    def __init__(self,x, y):
        super().__init__(IMG_PLAYER, PLAYER_SCALING)
        self.center_x = x
        self.center_y = y

class Laser(arcade.Sprite):
    def __init__(self,x, y):
        super().__init__(IMG_LASER, LASER_SCALING)
        self.center_x = x
        self.center_y = y



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_icon(pyglet_load(ICON_WINDOWS))
        arcade.set_background_color(arcade.color.BLACK)
        # OBJECT
        self.background = None
        self.player_list = None
        self.enemys_list = None
        self.lasers_list = None
        self.player = None
        # MOVE PLAYER
        self.left_pressed = False
        self.right_pressed = False
        # SETTING GAME
        self.level = 1
        self.score = 0
        self.highest_score = 0
        self.difficulty = 1
        # TEXT DRAW
        self.text_score = None
        self.text_highest_score = None
        self.text_level = None
        self.text_difficulty = None
        self.text_player_life = None

    def scoreboard(self):
        x_offset = 15
        y_offset = 100

        self.text_score = arcade.Text(f"Score: {self.score}",x_offset, y_offset, arcade.color.WHITE)
        self.text_highest_score = arcade.Text(f"Hi-Score: {self.highest_score}", x_offset,(y_offset-20),arcade.color.WHITE)
        self.text_level = arcade.Text(f"Level: {self.level}", x_offset, (y_offset - 40),
                                              arcade.color.WHITE)
        self.text_difficulty = arcade.Text(f"Difficulty: {self.difficulty}", x_offset, (y_offset - 60),
                                              arcade.color.WHITE)
        self.text_player_life = arcade.Text(f"Life: {self.player.life}", x_offset, (y_offset - 80),
                                           arcade.color.WHITE)

    def update_player_speed(self):
        self.player.change_x = 0

        if self.left_pressed:
            self.player.change_x = -PLAYER_SPEED
        elif self.right_pressed:
            self.player.change_x = PLAYER_SPEED

         # CHECK BOUNDS
        if self.player.center_x < self.player.width:
            self.player.center_x = self.player.width
        elif self.player.center_x + self.player.width > SCREEN_WIDTH:
            self.player.center_x = SCREEN_WIDTH - self.player.width

    def setup(self):
        self.background = arcade.load_texture(IMG_BACKGROUND)

        self.player_list = arcade.SpriteList()
        self.enemys_list = arcade.SpriteList()
        self.lasers_list = arcade.SpriteList()
        self.player = Player(25, 25)
        self.player_list.append(self.player)

        # INIT SCORE BOARD
        self.scoreboard()


    def on_draw(self):
        arcade.start_render()
        # DRAW BACKGROUND
        arcade.draw_lrwh_rectangle_textured(0,0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # DRAW TEXT
        self.text_score.draw()
        self.text_highest_score.draw()
        self.text_level.draw()
        self.text_difficulty.draw()
        self.text_player_life.draw()
        # DRAW TEXT
        self.player_list.draw()

    def on_update(self, delta_time: float):
        self.player_list.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif symbol == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif symbol == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()


def main():
    """Main function"""
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    game.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   """Main function"""
   main()

   #print(ICON_WINDOWS)