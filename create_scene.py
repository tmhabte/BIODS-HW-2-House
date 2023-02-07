#!/usr/bin/env python3
"""Draw a house scene using Turtle in Python.

Contributors:   Joseph Wakim, Ariana Tse, Thomas Habte, Angelika Hirsch,
Date:           January 30, 2023
For:            BIODS 253: Software Engineering for Scientists
Organization:   Stanford University

Notes
-----
Usage:  python create_scene.py <PATH_TO_PARAM_FILE>
Where:  <PATH_TO_PARAM_FILE> is a string path to a parameter file
"""

# Built-in libraries
import turtle
from typing import Tuple, Dict, Union, Optional

# Custom libraries
import src.doors as doors
import src.windows as windows
import src.tree_cloud as tree_cloud
import src.frame as frame
from src.util.shapes import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t", "--render_type", type=str, help="Render town before and after earthquake as well as original house"
)
args = parser.parse_args()

# Custom global parameters
SCREEN_DIM = 1000
Numeric = Union[float, int]
REQUIRED_PARAMS = [
    "house_width",
    "house_height",
    "roof_width",
    "door_height",
    "door_left_offset",
    "garage_1_left_offset",
    "garage_2_left_offset",
    "window_1_height",
    "window_1_width",
    "window_1_horizontal_offset",
    "window_1_vertical_offset",
    "window_2_height",
    "window_2_width",
    "window_2_horizontal_offset",
    "window_2_vertical_offset",
    "window_3_height",
    "window_3_width",
    "window_3_horizontal_offset",
    "window_3_vertical_offset",
    "window_4_height",
    "window_4_width",
    "window_4_horizontal_offset",
    "window_4_vertical_offset",
    "tree_1_horizontal_offset",
    "tree_1_vertical_offset",
    "tree_1_trunk_width",
    "tree_1_trunk_height",
    "tree_2_horizontal_offset",
    "tree_2_vertical_offset",
    "tree_2_trunk_width",
    "tree_2_trunk_height",
    "cloud_horizontal_offset",
    "cloud_vertical_offset",
    "cloud_bump_radius",
]


def read_from_param_file(path: Optional[str] = "scene_params.txt") -> Dict[str, Numeric]:
    """Read from a parameter file providing properties of the house.

    Notes
    -----
    The parameter file will specify the key dimensions of the house that
    the user would like to draw in the house scene. The file will have
    REQUIRED fields that must be specified. Lines of the parameter file
    will be ignored if they start with a "#" character.

    Parameters
    ----------
    path : Optional[str]
        A string path to the parameter file. If None, path will point to
        the default parameter file "scene_params.txt" in the root directory.

    Returns
    -------
    Dict[str, Numeric]
        A dictionary of the parameters specified in the parameter file.
    """
    # Open the parameter file
    with open(path, "r") as f:
        lines = f.readlines()

    # Parse parameters from file
    params = {}
    for line in lines:
        if line.startswith("#") or line == "\n":
            continue
        key, value = line.split("=")
        params[key.strip()] = float(value.strip())

    # Verify that required parameters are specified
    for param in REQUIRED_PARAMS:
        if param not in params.keys():
            print("missing required parameters:")
            print(param)
    return params


def draw_house(params: Dict[str, Numeric],
    start_coord: Tuple[float, float] = (SCREEN_DIM / 3, SCREEN_DIM / 3), scale: Numeric = 1, 
    angle = 0, earthquake = False):
    """Draws a house with a roof, 4 windows, 3 garage doors, one door.  
   
   Parameters
    ----------
    start_coord : Tuple[float, float]
        Bottom-left corner of the BASE of the house.
    params : Dict[str, Numeric]
        A dictionary of parameters specifying the dimensions of the house.
    scale : scale of house (0 to 1)
    angle : int or float
        The angle of the house.
    earthquake : bool
        If True, the house will be drawn with an earthquake effect.
    """
    scaled_params = params.copy()
    for key in scaled_params:
        scaled_params[key] *= scale

    # First, we compute the roof bottom left coordinates
    roof_bottom_left = (
        start_coord[0] - (scaled_params["roof_width"] - scaled_params["house_width"]) / 2,
        start_coord[1] + scaled_params["house_height"],
    )

    # Draw the frame of the house
    frame.draw_base(
        start_coord[0], start_coord[1], scaled_params["house_height"],
        scaled_params["house_width"], angle = angle)
    frame.draw_roof(
        roof_bottom_left[0], roof_bottom_left[1], scaled_params["roof_width"], angle = angle)

    # Draw a door
    doors.draw_door(
        start_coord[0] + scaled_params["door_left_offset"], start_coord[1],
        scaled_params["door_height"], angle = angle, earthquake = earthquake)

    # Draw two garage doors
    coordinates_garage_doors = [
        (start_coord[0] + scaled_params["garage_1_left_offset"], start_coord[1]),
        (start_coord[0] + scaled_params["garage_2_left_offset"], start_coord[1]),
    ]

    for x, y in coordinates_garage_doors:
        doors.draw_garage_door(x, y, scaled_params["garage_door_height"], angle = angle, earthquake = earthquake)

    # Draw windows
    for i in range(1, 5):
        x = start_coord[0] + scaled_params["window_{}_horizontal_offset".format(i)]
        y = start_coord[1] + scaled_params["window_{}_vertical_offset".format(i)]
        height = scaled_params["window_{}_height".format(i)]
        width = scaled_params["window_{}_width".format(i)]
        
        # Make two of the windows cracked only if there has been an earthquake
        if render_type == "with_earthquake" and i % 2 == 0:
            windows.draw_window(x, y, height, width, angle = angle, crack=True)
        else:
            windows.draw_window(x, y, height, width)

    turtle.end_fill()


def create_scene(
    render_type, params: Dict[str, Numeric], start_coord: Tuple[float, float] = (SCREEN_DIM / 3, SCREEN_DIM / 3), angle = 0
):
    """Create scene of house that includes required components.

    Notes
    -----
    Required components include: two garages, one door, and four windows,
    two trees, and a cloud.

    Parameters
    ----------
    start_coord : Tuple[float, float]
        Bottom-left corner of the BASE of the house.
    params : Dict[str, Numeric]
        A dictionary of parameters specifying the dimensions of the house.
    """
    # Draw lawn
    turtle.color("green")
    turtle.begin_fill()
    doors.draw_rectangle(
        start_pos_x=start_coord[0] - 3 * SCREEN_DIM,
        start_pos_y=start_coord[1] - 3 * SCREEN_DIM,
        height=3 * SCREEN_DIM,
        width=6 * SCREEN_DIM,
    )
    turtle.end_fill()

    # Draw houses
    coordinates_x = [start_coord[0]]
    y = start_coord[1]
    if render_type == "original":

        draw_house(params, (coordinates_x[0], y))

    elif render_type == "without_earthquake":
        coordinates_x += [start_coord[0] + 1.2 * params["house_width"], start_coord[0] + 2.4 * params["house_width"]]
        
        draw_house(params, (coordinates_x[0], y))
        draw_house(params, (coordinates_x[1], y), scale = 0.9)
        draw_house(params, (coordinates_x[2], y), scale = 1)
    elif render_type == "with_earthquake":
        # DUPLICATED CODE -- better to change
        coordinates_x += [
            start_coord[0] + 1.2 * params["house_width"],
            start_coord[0] + 2.4 * params["house_width"],
        ]

        draw_house(params, (coordinates_x[0], y), earthquake = False)
        draw_house(params, (coordinates_x[1], y), scale=0.9, earthquake = False)
        draw_house(params, (coordinates_x[2], y), angle = angle, earthquake = True)
        turtle.color('green')
        turtle.begin_fill()
        draw_rectangle(coordinates_x[2], y, -params["house_height"], params["house_width"], 
                           angle = angle)
        turtle.end_fill()

    else:
        raise Exception("Unknown render type for image")

    # Draw trees
    turtle.setheading(0)
    tree_cloud.draw_tree(
        start_coord[0] + params["tree_1_horizontal_offset"],
        start_coord[1] + params["tree_1_vertical_offset"],
        params["tree_1_trunk_width"],
        params["tree_1_trunk_height"],
    )
    tree_cloud.draw_tree(
        start_coord[0] + params["tree_2_horizontal_offset"],
        start_coord[1] + params["tree_2_vertical_offset"],
        params["tree_2_trunk_width"],
        params["tree_2_trunk_height"],
    )

    # Draw cloud
    if render_type != "with_earthquake":
        tree_cloud.draw_cloud(
            start_coord[0] + params["cloud_horizontal_offset"],
            start_coord[1] + params["cloud_vertical_offset"],
            params["cloud_bump_radius"],
        )


if __name__ == "__main__":
    """Create the house scene."""
    angle = 2.8
    render_type = args.render_type
    turtle.Screen().screensize(SCREEN_DIM, SCREEN_DIM)
    turtle.setworldcoordinates(
        -SCREEN_DIM, -SCREEN_DIM, turtle.window_width() + SCREEN_DIM, turtle.window_height() + SCREEN_DIM
    )
    turtle.Screen().bgcolor("lightblue")
    turtle.speed(10)
    params = read_from_param_file()
    create_scene(render_type, params, angle = 2.8)
    turtle.done()
