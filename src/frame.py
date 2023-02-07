"""Draw the base of the house and the roof of the house.

Contributors:   Joseph Wakim
Date:           January 30, 2023
For:            BIODS 253: Software Engineering for Scientists
Organization:   Stanford University

Notes
-----
This module includes functions for drawing the base walls of the house and the
roof of the house. Both entities will be defined with respect to their
bottom-left corners.
"""
import turtle
from .util.shapes import draw_rectangle


def draw_base(start_x, start_y, house_height, house_width, angle=0):
    """Draw the base of the house.

    Parameters
    ----------
    start_x : float
        x-coordinate of the bottom-left corner of the base of the house.
    start_y : float
        y-coordinate of the bottom-left corner of the base of the house.
    house_height : float
        Height of the base of the house.
    house_width : float
        Width of the base of the house.
    """
    turtle.color('black', "lightgray")
    turtle.begin_fill()
    draw_rectangle(start_x, start_y, house_height, house_width, tilt=angle)
    turtle.end_fill()


def draw_roof(start_pos_x, start_pos_y, roof_width, angle=0):
    """Draw the roof of the house.

    Notes
    -----
    The roof is an isosceles right triangle with the right angle at the
    top center position.

    Parameters
    ----------
    start_x : float
        x-coordinate of the bottom-left corner of the roof of the house.
    start_y : float
        y-coordinate of the bottom-left corner of the roof of the house.
    roof_width : float
        Width of the roof of the house.
    """
    turtle.goto(start_pos_x, start_pos_y)
    turtle.seth(angle)
    roof_angled_dim = roof_width / 2 ** 0.5
    turtle.color('black', "brown")
    turtle.begin_fill()
    turtle.forward(roof_width)
    turtle.left(135)    # This angle will never change
    turtle.forward(roof_angled_dim)
    turtle.left(90)     # This angle will never change
    turtle.forward(roof_angled_dim)
    turtle.end_fill()
