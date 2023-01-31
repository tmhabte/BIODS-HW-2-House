import turtle

from src.util.shapes import *

def run_all_tests():
    '''
    Runs all test. Test drawing rectangle function and drawing circle. Compares output canvases (.ps files) with originals
    '''
    test_rectangle()
    test_circle()

def test_rectangle():
    turtle.clear()
    start_pos_x = 0
    start_pos_y = 0
    height = 50
    width = 100
    draw_rectangle(start_pos_x, start_pos_y, height, width)
    rect_draw = turtle.getscreen()
    rect_draw.getcanvas().postscript(file=r"testdata/test/test_rectangle.ps")
    assert open(r"testdata/test/test_rectangle.ps").readlines()[10:] == open(r"testdata/true/true_rectangle.ps").readlines()[10:] # Skip metadata, first 10 lines

def test_circle():
    turtle.clear()
    radius= 50
    color= 'blue'
    fill_circle(radius, color)
    circle_draw = turtle.getscreen()
    circle_draw.getcanvas().postscript(file=r"testdata/test/test_circle.ps")
    assert open("testdata/test/test_circle.ps").readlines()[10:] == open("testdata/true/true_circle.ps").readlines()[10:]

if __name__ == "__main__":
    """Create the house scene.
    """
    run_all_tests()