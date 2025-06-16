from graphics import Window, Line, Point


class Cell():
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = window


    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.__win is None:
            return
        # Left Wall
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        # Right Wall
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        # Top Wall
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        # Bottom Wall
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        my_center = Point((self.__x1+self.__x2)/2, (self.__y1+self.__y2)/2)
        other_center = Point((to_cell.__x1+to_cell.__x2)/2, (to_cell.__y1+to_cell.__y2)/2)

        if self.__win is None:
            return

        self.__win.draw_line(Line(my_center, other_center), color)