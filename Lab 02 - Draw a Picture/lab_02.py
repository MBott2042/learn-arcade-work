# Import the "arcade" libray
import arcade

# Open up a window.
arcade.open_window(1000, 800, "Lab2 Solar System")

# Set the background color
arcade.set_background_color((15, 0, 20))

# ready to draw
arcade.start_render()

# --- drawing the orbits ---
# Rocky planets
arcade.draw_ellipse_outline(500, 400, 120, 110, (237, 237, 230))
arcade.draw_ellipse_outline(500, 400, 160, 140, (237, 237, 230))
arcade.draw_ellipse_outline(500, 400, 190, 180, (237, 237, 230))
arcade.draw_ellipse_outline(500, 400, 240, 210, (237, 237, 230))

# Gas Giants
"""The orbit for the gas planets are off center because they have enough mass that the point of orbit Is not at the 
center of the sun. Although it is mostly not noticeable when it comes to Uranus and Neptune, Saturn and jupiter 
are quite noticeable."""
arcade.draw_ellipse_outline(530, 390, 400, 370, (237, 237, 230))
arcade.draw_ellipse_outline(510, 395, 550, 500, (237, 237, 230))
arcade.draw_ellipse_outline(501, 400, 700, 650, (237, 237, 230))
arcade.draw_ellipse_outline(501, 400, 900, 800, (237, 237, 230))

# --- Drawing the celestial body's ---

# Drawing the Sun
arcade.draw_circle_filled(500, 400, 30, (245, 233, 15))

# Drawing Mercury
arcade.draw_circle_filled(558.5, 400, 4.5, (97, 87, 77))

# Drawing Venus
# Fun fact did you know that Venus is the third-brightest object in the sky.
arcade.draw_circle_filled(565, 360, 6, (120, 114, 35))

# Drawing Earth
arcade.draw_circle_filled(558, 330, 6.5, (83, 147, 224))

# Drawing Mars
# fun fact Mars has a Volcano the size of arizona.
arcade.draw_circle_filled(510, 296, 5, (235, 57, 21))

# Drawing Jupiter
# fun fact Jupiter actually has rings there just not very big.
arcade.draw_circle_filled(460, 220, 15, (250, 144, 122))

# Drawing Saturn
# fun fact saturn is not very dense to the point where if put in water it would float.
arcade.draw_circle_outline(375, 180, 15, (96, 97, 55), 5)
arcade.draw_circle_filled(375, 180, 8, (121, 122, 18))

# Drawing Uranus
"""fun fact Uranus poles are almost perfectly horizontal,
 which means it rolls like a ball around the sun."""
arcade.draw_circle_filled(280, 150, 7, (70, 204, 219))

# Drawing Neptune
# fun fact Neptune has a storm similar to Jupiter's great big red spot
arcade.draw_circle_filled(206.5, 100, 6.8, (47, 9, 235))

# --- Drawing spaceship ---

# magnify
# the lines make an arrow
arcade.draw_circle_outline(500, 240, 10, (245, 245, 245), 2)
arcade.draw_line(509, 243, 600, 280, (245, 245, 245), 2)
arcade.draw_line(600, 280, 580, 290, (245, 245, 245), 2)
arcade.draw_line(600, 280, 583, 255, (245, 245, 245), 2)

# Body
arcade.draw_rectangle_filled(500, 240, 4, 5, (195, 198, 199))
arcade.draw_rectangle_filled(620, 280, 10, 25, (195, 198, 199))
arcade.draw_ellipse_filled(620, 280, 7, 13, (12, 116, 168))

# Nose
arcade.draw_triangle_filled(620, 310, 615, 290, 625, 290, (195, 198, 199))

# Tail
arcade.draw_polygon_filled(((610, 250),
                            (615, 270),
                            (630, 250),
                            (625, 270),
                            ), (250, 90, 10))

# Finish Drawing
arcade.finish_render()

# keep the window up
arcade.run()
