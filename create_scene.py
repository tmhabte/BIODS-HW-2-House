import turtle
from typing import Tuple

import src.doors as doors
import src.windows as windows
import src.tree_cloud as tree_cloud

screen_dim = 500
turtle.Screen().screensize(screen_dim, screen_dim)
turtle.setworldcoordinates(-screen_dim, -screen_dim, turtle.window_width() + screen_dim, turtle.window_height() + screen_dim)
turtle.Screen().bgcolor("lightblue")

def create_scene(start_coord: Tuple[float, float] = (screen_dim / 3, screen_dim / 3)):
    """Create scene of house that includes two garages, one door, and four windows, two trees, and a cloud.

    Parameters
    ----------
    start_coord : Tuple[float, float]
        Bottom-left corner of the BASE of the house.
    """

    # Define dimensions
    house_width = 800
    house_height = 300
    roof_width = 850
    roof_angled_dim = roof_width / 2 ** 0.5
    roof_bottom_left = (start_coord[0] - 25, start_coord[1] + house_height)

    def draw_base():
        """Draw the base of the house.
        """
        turtle.color('black', "lightgray")
        turtle.begin_fill()
        doors.draw_rectangle(start_coord[0], start_coord[1], house_height, house_width)
        turtle.end_fill()

    def draw_roof():
        """Draw the roof of the house.
        """
        turtle.color('black', "brown")
        turtle.setpos(roof_bottom_left)
        turtle.begin_fill()
        turtle.setheading(0)
        turtle.forward(roof_width)
        turtle.left(135)
        turtle.forward(roof_angled_dim)
        turtle.left(90)
        turtle.forward(roof_angled_dim)
        turtle.end_fill()

    # Draw lawn
    turtle.color('green')
    turtle.begin_fill()
    doors.draw_rectangle(start_coord[0] - 700, start_coord[1] - 700, 700, 2000)
    turtle.end_fill()

    # Draw the frame of the house
    draw_base()
    draw_roof()

    # Draw a door
    doors.draw_door(start_coord[0] + 75, start_coord[1], house_height / 3)

    # Draw two garage doors
    doors.draw_garage_door(start_coord[0] + 300, start_coord[1], house_height * 1 / 2, 4, scale=1.1)
    doors.draw_garage_door(start_coord[0] + 500, start_coord[1], house_height * 1 / 2, 4, scale=1.1)

    # Draw windows
    windows.draw_window(start_coord[0] + 150, start_coord[1] + 100, 50, 50)
    windows.draw_window(start_coord[0] + 150, start_coord[1] + house_height * 3 / 4, 50, 50)
    windows.draw_window(start_coord[0] + 350, start_coord[1] + house_height * 3 / 4, 50, 50)
    windows.draw_window(start_coord[0] + 500, start_coord[1] + house_height * 3 / 4, 50, 50)
    turtle.end_fill()

    # Draw trees
    turtle.setheading(0)
    tree_cloud.draw_tree(start_coord[0] - 150, start_coord[1], house_height / 5, 3 * house_height / 5)
    tree_cloud.draw_tree(start_coord[0] - 450, start_coord[1], house_height / 5, 3 * house_height / 5)

    # Draw cloud
    tree_cloud.draw_cloud(start_coord[0] - 300, start_coord[1] + 500, 70, color="white")

if __name__ == "__main__":
    """Create the house scene.
    """
    create_scene()