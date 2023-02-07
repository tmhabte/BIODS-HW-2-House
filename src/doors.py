import turtle
from .util.shapes import *


def draw_door(height, scale = 0.4):
    '''
    Draws a door and doorknob
    :param start_pos_x: x position to begin drawing (lower left corner)
    :param start_pos_y: y position to begin drawing (lower left corner)
    :param height: height of the door
    :param scale: ratio of door width to height
    :return: None- draws
    '''
    width = height * scale
    turtle.color('black', 'brown')
    turtle.begin_fill()
    draw_rectangle(height, width)
    turtle.end_fill()
    turtle.penup()
    turtle.left(90)
    turtle.forward(3*width/4)
    turtle.left(90)
    turtle.forward(height/2)
    turtle.right(90)
    turtle.pendown()
    turtle.color('black', 'gold')
    turtle.begin_fill()
    turtle.circle(width/8)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)


def draw_garage_lines(start_pos_x,start_pos_y, end_pos_x):
    '''
    Draws lines on garage door
    :param start_pos_x: x position to begin drawing
    :param start_pos_y: y position to begin drawing
    :param end_pos_x: x position to end drawing
    :return: None- draws
    '''
    current_pos_x = turtle.pos()[0]
    current_pos_y = turtle.pos()[1]
    turtle.forward(current_pos_y - start_pos_y)
    turtle.left(90)
    turtle.forward(start_pos_x - current_pos_x)
    #turtle.setpos(start_pos_x, start_pos_y)
    turtle.pendown()
    turtle.forward(end_pos_x - start_pos_x)
    #turtle.setpos(end_pos_x, start_pos_y)
    turtle.right(90)
    turtle.penup()


def draw_garage_door(start_pos_x, start_pos_y, height, num_lines=4, scale = 1.1):
    '''
    Draws garage door
    :param start_pos_x: x position to begin drawing (lower left corner)
    :param start_pos_y: y position to begin drawing (lower left corner)
    :param height:
    :param width:
    :param num_lines: number of lines on garage door
    :return: None- draws
    '''
    width = height*scale
    turtle.begin_fill()
    turtle.color("black", "gray")
    draw_rectangle(start_pos_x, start_pos_y, height, width)
    turtle.end_fill
    for i in range(num_lines-1):
        draw_garage_lines(start_pos_x, start_pos_y + (height*(i+1))/num_lines, start_pos_x + width)


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
