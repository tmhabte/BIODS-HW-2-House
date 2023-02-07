import turtle


def fill_circle(radius, color):
    '''
    Draws a filled in circle
    : param radius: radius of circle
    : param color: color of circle
    '''
    turtle.penup()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_rectangle(start_pos_x, start_pos_y, height, width, tilt=0):
    '''
    Draws a rectangle
    :param start_pos_x: x position to begin drawing (lower left corner)
    :param start_pos_y: y position to begin drawing (lower left corner)
    :param height:
    :param width:
    :return: None- draws
    '''
    turtle.penup()
    # at the end of each shape, face to the right of the shape, move to
    # current_pos_x = turtle.pos()[0]
    # current_pos_y = turtle.pos()[1]
    # turtle.forward(current_pos_y - start_pos_y)
    # turtle.left(90)
    # turtle.forward(start_pos_x - current_pos_x)
    turtle.setpos(start_pos_x, start_pos_y)
    turtle.seth(tilt)
    turtle.pendown()
    #turtle.seth(0)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
    turtle.penup()

