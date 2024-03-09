""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 4
Wallhit_sound = arcade.load_sound("wallhiy.wav")
Click_sound = arcade.load_sound("click.wav")


def draw_stars(x, y):
    # --- Stars ---

    # Star
    arcade.draw_circle_filled(500 + x, 500 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(550 + x, 450 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(600 + x, 400 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(650 + x, 350 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(700 + x, 300 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(750 + x, 250 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(800 + x, 200 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(850 + x, 150 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(900 + x, 100 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(950 + x, 50 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(450 + x, 550 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(400 + x, 600 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(350 + x, 650 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(300 + x, 700 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(250 + x, 750 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(200 + x, 800 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(150 + x, 850 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(100 + x, 900 + y, 2.5, (255, 255, 255))
    arcade.draw_circle_filled(50 + x, 950 + y, 2.5, (255, 255, 255))


# Other shape
class Chip:
    def __init__(self, position_x, position_y, change_x, change_y, size, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.size = size
        self.color = color
        self.angle = 0

    def draw(self):

        arcade.draw_ellipse_filled(self.position_x, self.position_y, self.size, self.size, self.color, 10, self.angle)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

# stop chip from going past border
        if self.position_x < self.size:
            self.position_x = self.size
            arcade.play_sound(Wallhit_sound)
        if self.position_x > SCREEN_WIDTH - self.size:
            self.position_x = SCREEN_WIDTH - self.size
            arcade.play_sound(Wallhit_sound)
        if self.position_y < self.size:
            self.position_y = self.size
            arcade.play_sound(Wallhit_sound)
        if self.position_y > SCREEN_HEIGHT - self.size:
            self.position_y = SCREEN_HEIGHT - self.size
            arcade.play_sound(Wallhit_sound)


class Box:
    def __init__(self, position_x, position_y, size, color):
        self.position_x = position_x
        self.position_y = position_y
        self.size = size
        self.color = color
        self.angle = 0

    def draw(self):

        arcade.draw_rectangle_outline(self.position_x, self.position_y, self.size, self.size,
                                      self.color, 10, self.angle)


class MyGame(arcade.Window):
    """ Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)

        arcade.set_background_color((15, 0, 20))

        self.box = Box(400, 300, 50, arcade.color.BLUE_BELL)
        self.chip = Chip(500, 400, 0, 0, 50, arcade.color.GOLD)

# drawing everything
    def on_draw(self):
        arcade.start_render()
        # background stars
        draw_stars(100, 50)
        draw_stars(150, 100)
        draw_stars(200, 150)
        draw_stars(250, 200)
        draw_stars(300, 250)
        draw_stars(350, 300)
        draw_stars(400, 350)
        draw_stars(50, 0)
        draw_stars(0, -50)
        draw_stars(-50, -100)
        draw_stars(-100, -150)
        draw_stars(-150, -200)
        draw_stars(-200, -250)
        draw_stars(-250, -300)
        draw_stars(-300, -350)
        draw_stars(-350, -400)
        draw_stars(-400, -450)
        draw_stars(-450, -500)
        draw_stars(-500, -550)
        draw_stars(-550, -600)
        self.box.draw()
        self.chip.draw()

# mouse control
    def on_mouse_motion(self, x, y, dx, dy):
        self.box.position_x = x
        self.box.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """
        arcade.play_sound(Click_sound)
        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)

# keyboard control
    def update(self, delta_time):
        self.chip.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.chip.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.chip.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.chip.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.chip.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.chip.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.chip.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
