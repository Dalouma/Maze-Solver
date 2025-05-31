from graphics import Window, Line, Point
from maze import Cell

def main():
    win = Window(800, 800)
    # line = Line(Point(200,200), Point(600,600))
    # win.draw_line(line)
    cell = Cell(win)
    cell.draw(100, 100, 200, 200)
    cell2 = Cell(win)
    cell2.draw(150, 225, 525, 675)
    cell3 = Cell(win)
    cell3.draw(10, 10, 790, 790)
    cell.draw_move(cell2)
    cell.draw_move(cell3, True)

    # This runs the window after settings have been applied.
    # Window appearance must be determined before this is called.
    win.wait_for_close()

if __name__ == "__main__":
    main()