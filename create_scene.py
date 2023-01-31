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
    "house_width", "house_height", "roof_width"
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
        if line.startswith("#") or line == "":
            continue
        key, value = line.split("=")
        params[key.strip()] = float(value.strip())

    # Verify that required parameters are specified
    for param in REQUIRED_PARAMS:
        assert param in params.keys()
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

    # Define dimensions
    house_width = params["house_width"]
    house_height = params["house_height"]
    roof_width = params["roof_width"]
    roof_bottom_left = (
        start_coord[0] - (roof_width - house_width/2), start_coord[1] + house_height
    )

    # Draw lawn
    turtle.color('green')
    turtle.begin_fill()
    doors.draw_rectangle(start_coord[0] - 700, start_coord[1] - 700, 700, 2000)
    turtle.end_fill()

    # Draw the frame of the house
    frame.draw_base(start_coord[0], start_coord[1], house_height, house_width)
    frame.draw_roof(roof_bottom_left[0], roof_bottom_left[1], roof_width)

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
    turtle.Screen().screensize(screen_dim, screen_dim)
    turtle.setworldcoordinates(-screen_dim, -screen_dim, turtle.window_width() + screen_dim, turtle.window_height() + screen_dim)
    turtle.Screen().bgcolor("lightblue")
    create_scene()