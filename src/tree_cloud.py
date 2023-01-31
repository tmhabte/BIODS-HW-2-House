import turtle
import src.doors as doors
DEFAULT_DIRECTION=0

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

def row_of_circles(num_circles, radius, color):
    '''
    Draws a horizontal row of circles
    : param num_circles: number of circles in row
    : param radius: radius of circles
    : param color: color of circles
    '''
    for i in range(num_circles):
        fill_circle(radius, color)
        x, y = turtle.pos()
        turtle.setpos(x + radius, y)

def draw_cloud(start_pos_x, start_pos_y, size, color='white'):
    '''
    Draws a cloud
    : param start_pos_x: starting x-position of turtle (Lower left hand corner of cloud)
    : param start_pos_y: starting y-position of turtle (Lower left hand corner of cloud)
    : param size: radius of circles used to make cloud
    : param color: color of circles used to make cloud
    '''
    turtle.penup()
    turtle.setpos(start_pos_x, start_pos_y)
    turtle.setheading(DEFAULT_DIRECTION)

    row_of_circles(3, size, color)
    turtle.setpos(start_pos_x+0.5*size, start_pos_y+size)
    row_of_circles(2, size, color)


def draw_tree(start_pos_x, start_pos_y, trunk_width, trunk_height, trunk_color='brown', foliage_color='green'):
    '''
    Draws a tree
    : param start_pos_x: starting x-position of turtle (Lower left hand corner of trunk)
    : param start_pos_y: starting y-position of turtle (Lower left hand corner of trunk)
    : param trunk_width: width of trunk
    : param trunk_height: height of trunk
    : param trunk_color: color of trunk
    : param foliage_color: color of foliage
    '''
    turtle.penup()
    turtle.setpos(start_pos_x, start_pos_y)
    turtle.setheading(DEFAULT_DIRECTION)

    # Draw Tree trunk
    turtle.color(trunk_color)
    turtle.begin_fill()
    doors.draw_rectangle(start_pos_x, start_pos_y, trunk_height, trunk_width)
    turtle.end_fill()

    # Draw foliage
    turtle.setheading(DEFAULT_DIRECTION)
    draw_cloud(start_pos_x-0.5*trunk_width, start_pos_y+0.75*trunk_height, trunk_width, foliage_color)




