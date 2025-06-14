from graphics import Window, Line, Point
from maze import Maze

def main():
    win = Window(800, 800)
    # line = Line(Point(200,200), Point(600,600))
    # win.draw_line(line)
    # cell = Cell(win)
    # cell.draw(100, 100, 200, 200)
    # cell2 = Cell(win)
    # cell2.draw(150, 225, 525, 675)
    # cell3 = Cell(win)
    # cell3.draw(10, 10, 790, 790)
    # cell.draw_move(cell2)
    # cell.draw_move(cell3, True)
    maze = Maze(100, 100, 10, 10, 50, 50, win)
    maze._animate()

    # This runs the window after settings have been applied.
    # Window appearance must be determined before this is called.
    win.wait_for_close()

if __name__ == "__main__":
    main()