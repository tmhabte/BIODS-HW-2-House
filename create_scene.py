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

# Custom global parameters
SCREEN_DIM = 500
Numeric = Union[float, int]
REQUIRED_PARAMS = [
    "house_width", "house_height", "roof_width", "door_height",
    "door_left_offset", "garage_1_left_offset", "garage_2_left_offset",
    "window_1_height", "window_1_width", "window_1_horizontal_offset",
    "window_1_vertical_offset", "window_2_height", "window_2_width",
    "window_2_horizontal_offset", "window_2_vertical_offset",
    "window_3_height", "window_3_width", "window_3_horizontal_offset",
    "window_3_vertical_offset", "window_4_height", "window_4_width",
    "window_4_horizontal_offset", "window_4_vertical_offset",
    "tree_1_horizontal_offset", "tree_1_vertical_offset", "tree_1_trunk_width",
    "tree_1_trunk_height", "tree_2_horizontal_offset", "tree_2_vertical_offset",
    "tree_2_trunk_width", "tree_2_trunk_height", "cloud_horizontal_offset",
    "cloud_vertical_offset", "cloud_bump_radius"
]


def read_from_param_file(
    path: Optional[str] = "scene_params.txt"
) -> Dict[str, Numeric]:
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


def create_scene(
    params: Dict[str, Numeric],
    start_coord: Tuple[float, float] = (SCREEN_DIM / 3, SCREEN_DIM / 3)
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
    roof_bottom_left = (
        start_coord[0] - (
                params["roof_width"] - params["house_width"]
        )/2, start_coord[1] +
        params["house_height"]
    )

    # Draw lawn
    turtle.color('green')
    turtle.begin_fill()
    doors.draw_rectangle(
        start_pos_x=start_coord[0] - 3 * SCREEN_DIM,
        start_pos_y=start_coord[1] - 3 * SCREEN_DIM,
        height=3 * SCREEN_DIM,
        width=6 * SCREEN_DIM
    )
    turtle.end_fill()

    # Draw the frame of the house
    frame.draw_base(
        start_coord[0], start_coord[1], params["house_height"],
        params["house_width"]
    )
    frame.draw_roof(
        roof_bottom_left[0], roof_bottom_left[1], params["roof_width"]
    )

    # Draw a door
    doors.draw_door(
        start_coord[0] + params["door_left_offset"], start_coord[1],
        params["door_height"]
    )

    # Draw two garage doors
    doors.draw_garage_door(
        start_coord[0] + params["garage_1_left_offset"], start_coord[1],
        params["garage_door_height"]
    )
    doors.draw_garage_door(
        start_coord[0] + params["garage_2_left_offset"], start_coord[1],
        params["garage_door_height"]
    )

    # Draw windows
    windows.draw_window(
        start_coord[0] + params["window_1_horizontal_offset"],
        start_coord[1] + params["window_1_vertical_offset"],
        params["window_1_height"], params["window_1_width"]
    )
    windows.draw_window(
        start_coord[0] + params["window_2_horizontal_offset"],
        start_coord[1] + params["window_2_vertical_offset"],
        params["window_2_height"], params["window_2_width"]
    )
    windows.draw_window(
        start_coord[0] + params["window_3_horizontal_offset"],
        start_coord[1] + params["window_3_vertical_offset"],
        params["window_3_height"], params["window_3_width"]
    )
    windows.draw_window(
        start_coord[0] + params["window_4_horizontal_offset"],
        start_coord[1] + params["window_4_vertical_offset"],
        params["window_4_height"], params["window_4_width"]
    )
    turtle.end_fill()

    # Draw trees
    turtle.setheading(0)
    tree_cloud.draw_tree(
        start_coord[0] + params["tree_1_horizontal_offset"],
        start_coord[1] + params["tree_1_vertical_offset"],
        params["tree_1_trunk_width"], params["tree_1_trunk_height"]
    )
    tree_cloud.draw_tree(
        start_coord[0] + params["tree_2_horizontal_offset"],
        start_coord[1] + params["tree_2_vertical_offset"],
        params["tree_2_trunk_width"], params["tree_2_trunk_height"]
    )

    # Draw cloud
    tree_cloud.draw_cloud(
        start_coord[0] + params["cloud_horizontal_offset"],
        start_coord[1] + params["cloud_vertical_offset"],
        params["cloud_bump_radius"]
    )

if __name__ == "__main__":
    """Create the house scene.
    """
    turtle.Screen().screensize(SCREEN_DIM, SCREEN_DIM)
    turtle.setworldcoordinates(-SCREEN_DIM, -SCREEN_DIM, turtle.window_width() + SCREEN_DIM, turtle.window_height() + SCREEN_DIM)
    turtle.Screen().bgcolor("lightblue")
    params = read_from_param_file()
    create_scene(params)
    turtle.done()