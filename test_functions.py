import turtle

import src.doors as doors
import src.windows as windows
import src.tree_cloud as tree_cloud

def run_all_tests():
    test_rectangle()
    test_circle()

def test_rectangle():
    turtle.clear()
    start_pos_x = 0
    start_pos_y = 0
    height = 50
    width = 100
    doors.draw_rectangle(start_pos_x, start_pos_y, height, width)
    rect_draw = turtle.getscreen()
    rect_draw.getcanvas().postscript(file=r"test/test/test_rectangle.ps")
    assert open(r"test/test/test_rectangle.ps").readlines()[10:] == open(r"test/true/true_rectangle.ps").readlines()[10:]

def test_circle():
    turtle.clear()
    radius= 50
    color= 'blue'
    tree_cloud.fill_circle(radius, color)
    circle_draw = turtle.getscreen()
    circle_draw.getcanvas().postscript(file=r"test/test/test_circle.ps")
    assert open("test/test/test_circle.ps").readlines()[10:] == open("test/true/true_circle.ps").readlines()[10:]

if __name__ == "__main__":
    """Create the house scene.
    """
    run_all_tests()