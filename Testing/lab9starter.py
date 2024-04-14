
import random
import arcade
from pyglet.math import Vec2

"""
Scroll around a large screen.
Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""
"""
Lab 9 Step 1 - Start with one of these example: 
This example is the recommended one. You are welcome to start with the 
third example but it is a bit more complex. The first example is not
challenging enough and will be graded more stringently if selected.
"""
SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 10000
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "RUN BOY RUN"
good_sound = arcade.load_sound("good.wav")
# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
NUMBER_OF_COINS = 50

PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """
    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)


        self.all_sprites_list = None
        self.coin_list = None


        # Sprite lists
        self.player_list = None
        self.wall_list = None
        # Set up the player
        self.player_sprite = None
        self.score = 0

        self.elapsed_ms = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0


        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        #the walls
        # Place boxes inside a loop
        for x in range(0,1700, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png",)
            wall.center_x = x
            wall.center_y = -100
            self.wall_list.append(wall)
        # --- Place walls with a list
        for y in range(0,1700, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png",)
            wall.center_x = -100
            wall.center_y = y
            self.wall_list.append(wall)
        # --- Place walls with a list
        for x in range(0, 1700, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", )
            wall.center_x = x
            wall.center_y = 1700
            self.wall_list.append(wall)
        # --- Place walls with a list
        for y in range(0, 1700, 64):
            wall = arcade.Sprite(":resources:images/tiles/stoneCenter.png", )
            wall.center_x = 1700
            wall.center_y = y
            self.wall_list.append(wall)
        # --- Place walls with a list
        # coins not in walls

        """
        Lab 9 Step 2 -- Delete the current wall placement code and create
        your own
        
        Lab 9 Step 3
        Create a more complex arrangement of walls. Make sure the walls don’t
        allow the user to go off-screen. This is worth 6 points, based on how
        complex the arrangement. See Individually Placing Walls, Placing Walls
        With A Loop, and Placing Walls With A List for ideas. Just DON’T do
        the same thing as examples. Make it your own. Specifically, do NOT 
        just copy the random wall-gap algorithm in the scrolling screen example.
        """
        # -- Set up several columns of walls
        for y in range(200, 1650, 210):
            for x in range(0, 400, 64):
                wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in range(200, 1650, 210):
            for x in range(600, 1200, 64):
                wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for y in range(200, 1650, 210):
            for x in range(1400, 1650, 64):
                wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for x in range(490, 600, 210):
            for y in range(0, 1650, 432):
                wall = arcade.Sprite(":resources:images/tiles/lava.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for x in range(1290, 1400, 210):
            for y in range(0, 1650, 432):
                wall = arcade.Sprite(":resources:images/tiles/lava.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        for x in range(900, 1200, 432):
                for y in range(200, 1450, 64):
                    wall = arcade.Sprite(":resources:images/tiles/lava.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
        for i in range(NUMBER_OF_COINS):
            coin = arcade.Sprite(":resources:images/items/star.png", )
            coin_placed_successfully = False
            while not coin_placed_successfully:
                coin.center_x = random.randrange(0, 1700, 64)
                coin.center_y = random.randrange(0, 1700, 64)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True
            self.coin_list.append(coin)

        """ 
        Step 4 - Update the graphics. Choose different blocks for wall segments
        Change the character, etc., Remember you only need one wall list, but
        each sprite graphic in the list can be different if you want it to be.
        """
        """
        Step 5 - Add coins or something to collect. Be careful to not place coins
        on wall segments where player can't collect. See example for how to avoid 
        this.
        """
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """
        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()



        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=700, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

        if len(self.coin_list) == 0:
            arcade.draw_text("GAME", 0, 300, arcade.color.ROSE, 200)
            arcade.draw_text("OVER", 0, 50, arcade.color.ROSE, 200)

        """
        Step 6 - Keep a score of how many coins were collected and display on screen.
        """

        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # print message every 1 second
        self.elapsed_ms += delta_time
        if self.elapsed_ms > 1:
            print("One second tick")
            self.elapsed_ms = 0

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if len(self.coin_list) != 0:
            self.coin_list.update()
            # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        if len(self.coin_list) != 0:
            # Loop through each colliding sprite, remove it, and add to the score.
            for coin in coins_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(good_sound)
        """
        Step 7 - Play a sound each time the user collects a coin. To do that
        monitor for collisions between player and coin, remove coin, update score,
        and play sound.
        """
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a
        smoother pan. This is referring to the CAMERA_SPEED define.
        """
        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))



def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()