"""Draw windows into a Turtle scene

Author:		Joseph Wakim
Date:		January 23, 2023
For:		BIODS 253
"""

import turtle
from typing import Tuple
import src.doors as doors

RIGHT_DIRECTION=0
UP_DIRECTION=90

def draw_window(
    lower_left: Tuple[float, float],
    width: float,
    height: float,
    color = 'white',
    outline_color= 'black'
):
    """Draw a window in a turtle scene.
    
    Notes
    -----
    The window is drawn into the active turtle object, which is
    handled as a globle parameter.
    
    Parameters
    ----------
    lower_left : Tuple[float, float]
        Lower left coordinate of the window in the scene, in the
        form (x, y)
    width : float
        Width of the window
    height : float
        Height of the window
    """

    def draw_center_height():
        center_height = lower_left[1] + (height/2)
        turtle.penup()
        turtle.goto(lower_left[0], center_height)
        turtle.setheading(RIGHT_DIRECTION)
        turtle.pendown()
        turtle.forward(width)
        turtle.penup()
        

    def draw_center_width():
        center_width = lower_left[0] + (width/2)
        turtle.penup()
        turtle.goto(center_width, lower_left[1])
        turtle.setheading(UP_DIRECTION)
        turtle.pendown()
        turtle.forward(height)
        turtle.penup()

    turtle.penup()
    turtle.goto(lower_left)

    turtle.color(outline_color, color)
    turtle.begin_fill()
    doors.draw_rectangle(lower_left[0], lower_left[1], height, width)
    turtle.end_fill()

    draw_center_height()
    draw_center_width()
