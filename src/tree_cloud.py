import turtle

def fill_circle(size, color):
    '''
    Draws a filled in circle
    : param size: radius of circle
    : param color: color of circle
    '''
    turtle.penup()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def draw_cloud(start_pos_x, start_pos_y, size, color):
    '''
    Draws a cloud
    : param start_pos_x: starting x-position of turtle (Lower left hand corner of cloud)
    : param start_pos_y: starting y-position of turtle (Lower left hand corner of cloud)
    : param size: radius of circle
    : param color: color of circle
    '''
    turtle.penup()
    turtle.setpos(start_pos_x, start_pos_y)

    # Circle 1
    fill_circle(size, color)

    # Move to position of second circle in cluster (2nd circle, bottom row)
    turtle.forward(size * (6 / 5))
    turtle.right(90)
    turtle.forward(size / 4)
    turtle.left(90)

    # Circle 2
    fill_circle(size * 1.1, color)

    # Move to position of third circle in cluster (3rd circle, bottom row)
    turtle.forward(size * (6 / 5))

    # Circle 3
    fill_circle(size, color)

    # Move to position of 4th circle in cluster (1st circle, top row)
    turtle.left(90)
    turtle.forward(size * (6.5 / 5))
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.right(180)

    smaller_size = size * 4 / 5

    # Circle 4
    fill_circle(smaller_size, color)

    # Move to position of 5th circle in cluster (2nd circle, top row)
    turtle.forward(smaller_size * 1.6)

    # Circle 5
    fill_circle(smaller_size * 1.2, color)


def draw_tree(start_pos_x, start_pos_y, size):
    '''
    Draws a tree
    : param start_pos_x: starting x-position of turtle (Upper left hand corner of trunk)
    : param start_pos_y: starting y-position of turtle (Upper left hand corner of trunk)
    : param size: radius of circle
    : param color: color of circle
    '''
    turtle.penup()
    turtle.setpos(start_pos_x, start_pos_y)

    # Draw Tree trunk
    turtle.color('brown')
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(3 * size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(3 * size)
    turtle.end_fill()

    # Move to top of trunk to draw foliage
    turtle.left(90)
    turtle.forward(size * 0.75)
    turtle.left(90)
    turtle.forward(size * 0.25)
    turtle.left(90)

    x, y = turtle.pos()

    # Draw cloud in green as foliage
    draw_cloud(x, y, size, 'green')




