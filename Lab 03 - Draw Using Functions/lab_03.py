# Import the "arcade" libray
import arcade


def draw_space_ship(x, y):
    # --- Drawing spaceship ---

    # Body
    arcade.draw_rectangle_filled(500 + x, 75 + y, 46, 75, (195, 198, 199))
    arcade.draw_ellipse_filled(500 + x, 75 + y, 20, 45, (12, 116, 168))

    # Nose
    arcade.draw_triangle_filled(500 + x, 160 + y, 477 + x, 110 + y, 523 + x, 110 + y, (195, 198, 199))

    # Tail
    arcade.draw_polygon_filled(((465 + x, 0 + y),
                                (478 + x, 41 + y),
                                (535 + x, 0 + y),
                                (524 + x, 41 + y),
                                ), (250, 90, 10))


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


def on_draw(delta_time):
    # ready to draw
    arcade.start_render()

    draw_stars(100, 50)
    draw_stars(150, 100)
    draw_stars(200, 150)
    draw_stars(250, 200)
    draw_stars(300, 250)
    draw_stars(350, 300)
    draw_stars(400, 350)
    draw_stars(50, 0)
    draw_stars(0,  -50)
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
    draw_space_ship(0, on_draw.space_ship1_x)

    on_draw.space_ship1_x = (on_draw.space_ship1_x + 5) % 800


on_draw.space_ship1_x = 150


def main():
    # Open up a window.
    arcade.open_window(1000, 800, "Lab3 Rocket in Route")

    # Set the background color
    arcade.set_background_color((15, 0, 20))

    # Call on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# call the main function to get the program started
main()
