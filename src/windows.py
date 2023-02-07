"""Draw windows into a Turtle scene

Author:		Joseph Wakim
Date:		January 23, 2023
For:		BIODS 253
"""

import turtle
from .util.shapes import *

RIGHT_DIRECTION=0
UP_DIRECTION=90

def draw_window(
    start_pos_x: float,
    start_pos_y: float,
    width: float,
    height: float,
    color = 'white',
    outline_color= 'black', 
    angle = 0
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
    color : str
        Color of the window
    outline_color : str 
        Color of the outline of the window
    angle : float   
        Angle of the window
    """

    def draw_center_height():
        center_height = start_pos_y + (height/2)
        turtle.penup()
        turtle.goto(start_pos_x, center_height)
        turtle.setheading(RIGHT_DIRECTION + angle)
        turtle.pendown()
        turtle.forward(width)
        turtle.penup()
        

    def draw_center_width():
        center_width = start_pos_x + (width/2)
        turtle.penup()
        turtle.goto(center_width, start_pos_y)
        turtle.setheading(UP_DIRECTION + angle)
        turtle.pendown()
        turtle.forward(height)
        turtle.penup()

    turtle.penup()
    turtle.goto(start_pos_x, start_pos_y)

    turtle.color(outline_color, color)
    turtle.begin_fill()
    draw_rectangle(start_pos_x, start_pos_y, height, width, angle = angle)
    turtle.end_fill()

    draw_center_height()
    draw_center_width()
