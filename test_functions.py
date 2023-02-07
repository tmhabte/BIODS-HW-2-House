import turtle
import unittest

from src.util.shapes import *
from src.windows import *


class TestShapeDrawings(unittest.TestCase):
    def test_rectangle(self):
        turtle.clear()
        start_pos_x = 0
        start_pos_y = 0
        height = 50
        width = 100
        draw_rectangle(start_pos_x, start_pos_y, height, width)
        rect_draw = turtle.getscreen()
        rect_draw.getcanvas().postscript(file=r"testdata/test/test_rectangle.ps")

        self.assertEqual(
            open(r"testdata/test/test_rectangle.ps").readlines()[10:],
            open(r"testdata/true/true_rectangle.ps").readlines()[10:],
        )  # Skip metadata, first 10 lines

    def test_circle(self):
        turtle.clear()
        radius = 50
        color = "blue"
        fill_circle(radius, color)
        circle_draw = turtle.getscreen()
        circle_draw.getcanvas().postscript(file=r"testdata/test/test_circle.ps")
        self.assertEqual(
            open(r"testdata/test/test_circle.ps").readlines()[10:],
            open(r"testdata/true/true_circle.ps").readlines()[10:],
        )  # Skip metadata, first 10 lines

    def test_rectangle_rotate_30(self):
        """add a unit test to see if rotation of a rectangle of 30 degrees works properly"""
        turtle.clear()
        draw_rectangle(start_pos_x=0, start_pos_y=0, height=50, width=100, angle=30)
        rect_draw = turtle.getscreen()
        rect_draw.getcanvas().postscript(file=r"testdata/test/test_rectangle_rotate_30.ps")

        self.assertEqual(
            open(r"testdata/test/test_rectangle_rotate_30.ps").readlines()[10:],
            open(r"testdata/true/true_rectangle_rotate_30.ps").readlines()[10:],
        )

    def test_rectangle_rotate_2(self):
        """add a unit test to see if rotation of a rectangle of 2 degrees works properly"""
        turtle.clear()
        draw_rectangle(start_pos_x=0, start_pos_y=0, height=50, width=100, angle=2)
        rect_draw = turtle.getscreen()
        rect_draw.getcanvas().postscript(file=r"testdata/test/test_rectangle_rotate_2.ps")

        self.assertEqual(
            open(r"testdata/test/test_rectangle_rotate_2.ps").readlines()[10:],
            open(r"testdata/true/true_rectangle_rotate_2.ps").readlines()[10:],
        )

    def test_draw_window(self):
        """add a unit test to see if cracked window works properly"""
        turtle.clear()
        draw_window(start_pos_x=0, start_pos_y=0, height=50, width=50, crack=True)
        img = turtle.getscreen()
        img.getcanvas().postscript(file=r"testdata/test/test_window_cracked.ps")

        self.assertEqual(
            open(r"testdata/test/test_window_cracked.ps").readlines()[10:],
            open(r"testdata/true/true_window_cracked.ps").readlines()[10:],
        )


if __name__ == "__main__":
    unittest.main()
