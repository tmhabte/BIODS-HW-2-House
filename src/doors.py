import turtle
from .util.shapes import *


def draw_door(start_pos_x, start_pos_y, height, scale = 0.4, angle=0, earthquake = False):
    '''
    Draws a door and doorknob
    :param start_pos_x: x position to begin drawing (lower left corner)
    :param start_pos_y: y position to begin drawing (lower left corner)
    :param height: height of the door
    :param scale: ratio of door width to height
    :param angle: angle of door
    :return: None- draws
    '''
    width = height * scale
    turtle.color('black', 'brown')
    turtle.begin_fill()
    if earthquake:
        start_pos_y = start_pos_y + height/20
    draw_rectangle(start_pos_x, start_pos_y, height, width, angle)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(start_pos_x+3*width/4, start_pos_y+height/2)
    turtle.seth(0)
    turtle.pendown()
    turtle.color('black', 'gold')
    turtle.begin_fill()
    turtle.circle(width/8)
    turtle.end_fill()
    turtle.penup()


def draw_garage_lines(start_pos_x,start_pos_y, end_pos_x, angle=0):
    '''
    Draws lines on garage door
    :param start_pos_x: x position to begin drawing
    :param start_pos_y: y position to begin drawing
    :param end_pos_x: x position to end drawing
    :return: None- draws
    '''
    turtle.setpos(start_pos_x, start_pos_y)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(end_pos_x-start_pos_x)
    turtle.penup()


def draw_garage_door(start_pos_x, start_pos_y, height, num_lines=4, scale = 1.1, angle=0, earthquake = False):
    '''
    Draws garage door
    :param start_pos_x: x position to begin drawing (lower left corner)
    :param start_pos_y: y position to begin drawing (lower left corner)
    :param height:
    :param width:
    :param num_lines: number of lines on garage door
    :param scale: ratio of garage door width to height
    :param angle: angle of garage door
    :param earthquake: whether or not to draw lines with earthquake effect
    :return: None- draws
    '''
    width = height*scale
    turtle.begin_fill()
    turtle.color("black", "gray")
    if earthquake:
        start_pos_y = start_pos_y + height/8
    draw_rectangle(start_pos_x, start_pos_y, height, width, angle)
    turtle.end_fill
    for i in range(num_lines-1):
        draw_garage_lines(start_pos_x, start_pos_y + (height*(i+1))/num_lines, start_pos_x + width, angle)


if __name__ == "__main__":
    """ Demonstrate how doors appear.
    """
    
    turtle.color('pink', 'tan')

    # Sample parameters
    door_height = 50
    door_x = 10
    door_y = 0

    garage_x = -200
    garage_y = 0
    garage_height = door_height * 1.3
    garage_lines = 4

    draw_door(door_x,door_y,door_height)
    draw_garage_door(garage_x, garage_y, garage_height, garage_lines)

    turtle.done()
