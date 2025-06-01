from graphics import Window, Line, Point
import time


class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

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

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        my_center = Point((self.__x1+self.__x2)/2, (self.__y1+self.__y2)/2)
        other_center = Point((to_cell.__x1+to_cell.__x2)/2, (to_cell.__y1+to_cell.__y2)/2)

        if self.__win is None:
            return

        self.__win.draw_line(Line(my_center, other_center), color)

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        self.__cells = [ [Cell(self.__win) for _ in range(self.__num_rows)] for _ in range(self.__num_cols) ]
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        x1 = i * self.__cell_size_x + self.__x1
        y1 = j * self.__cell_size_y + self.__y1
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.__win is None:
            return

        self.__win.redraw()
        time.sleep(0.01)
        