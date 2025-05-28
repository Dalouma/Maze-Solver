from graphics import Window, Line, Point

def main():
    win = Window(800, 800)
    line = Line(Point(200,200), Point(600,600))
    win.draw_line(line)

    # This runs the window after settings have been applied.
    # Window appearance must be determined before this is called.
    win.wait_for_close()

if __name__ == "__main__":
    main()