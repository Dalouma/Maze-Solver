from graphics import Window, Line, Point
from maze import Maze

def main():
    win = Window(800, 800)
    maze = Maze(100, 100, 25, 25, 20, 20, win)
    maze.solve()

    # This runs the window after settings have been applied.
    # Window draw functions must be handled before this is called.
    win.wait_for_close()

if __name__ == "__main__":
    main()