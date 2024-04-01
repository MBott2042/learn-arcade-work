import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = .25
SPRITE_SCALING_METEOR = .25
COIN_COUNT = 50
METEOR_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins Example"
good_sound = arcade.load_sound("good.wav")
bad_sound = arcade.load_sound("bad.wav")


class Coin(arcade.Sprite, ):
    def update(self):

        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)


class Meteor(arcade.Sprite):
    def update(self):
        # Move the meteor
        self.center_y -= 1
        self.center_x -= 1
        # See if the meteor has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            # Reset the meteor to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20)
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.meteor_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color((15, 0, 20))

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        img = ":resources:images/space_shooter/playerShip1_orange.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/items/star.png",
                        SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(METEOR_COUNT):
            # Create the meteor instance
            # Coin image from kenney.nl
            meteor = Meteor(":resources:images/space_shooter/meteorGrey_big3.png", SPRITE_SCALING_METEOR)

            # Position the meteor
            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the meteor to the lists
            self.meteor_list.append(meteor)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.meteor_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

        if len(self.coin_list) == 0:
            arcade.draw_text("GAME", 0, 300, arcade.color.ROSE, 200)
            arcade.draw_text("OVER", 0, 50, arcade.color.ROSE, 200)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        if len(self.coin_list) != 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

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

        meteor_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.meteor_list)
        if len(self.coin_list) != 0:
            self.meteor_list.update()
        # Loop through each colliding sprite, remove it, and add to the score.
        for meteor in meteor_hit_list:
            meteor.remove_from_sprite_lists()
            self.score += -1
            arcade.play_sound(bad_sound)
        if len(self.coin_list) == 0:
            for meteor in meteor_hit_list:
                meteor.remove_from_sprite_lists()
                self.score += -1
                arcade.play_sound(bad_sound)


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
