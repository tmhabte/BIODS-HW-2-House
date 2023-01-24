"""Draw windows into a Turtle scene

Author:		Joseph Wakim
Date:		January 23, 2023
For:		BIODS 253
"""

import turtle as t
from typing import Tuple


def draw_window(
    lower_left: Tuple[float, float],
    width: float,
    height: float
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
        t.penup()
        t.goto(lower_left[0], center_height)
        t.setheading(0)
        t.pendown()
        t.forward(width)
        t.penup()
        

    def draw_center_width():
        center_width = lower_left[0] + (width/2)
        t.penup()
        t.goto(center_width, lower_left[1])
        t.setheading(90)
        t.pendown()
        t.forward(height)
        t.penup()
        
    def draw_frame():
        t.penup()
        t.color("black", "white")
        t.begin_fill()
        t.goto(lower_left)
        t.setheading(0)
        t.pendown()
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.penup()
        t.end_fill()
    
    t.penup()
    t.goto(lower_left)
    draw_frame()
    draw_center_height()
    draw_center_width()
