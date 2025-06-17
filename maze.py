from cell import Cell
import time, random


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
        seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        if seed is not None:
            random.seed(seed)

        self.__cells = []
        self.__create_cells()

        self.__break_entrance_and_exit()
        if num_cols > 0 and num_rows > 0:
            self.__break_walls_r(0, 0)
            self.__reset_cells_visited()        

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
        
    def __break_entrance_and_exit(self):
        if self.__num_cols > 0:
            self.__cells[0][0].has_top_wall = False
            self.__draw_cell(0, 0)
            self.__cells[-1][-1].has_bottom_wall = False
            self.__draw_cell(self.__num_cols-1, self.__num_rows-1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            possible_directions = []
            # UP
            if j - 1 >= 0 and self.__cells[i][j-1].visited == False:
                possible_directions.append((i, j-1))
            # DOWN
            if j + 1 < self.__num_rows and self.__cells[i][j+1].visited == False:
                possible_directions.append((i, j+1))
            # LEFT
            if i - 1 >= 0 and self.__cells[i-1][j].visited == False:
                possible_directions.append((i-1, j))
            # RIGHT
            if i + 1 < self.__num_cols and self.__cells[i+1][j].visited == False:
                possible_directions.append((i+1, j))

            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return
            
            dir = random.choice(possible_directions)

            # UP
            if dir[1] == j-1:
                self.__cells[i][j].has_top_wall = False
            # DOWN
            if dir[1] == j+1:
                self.__cells[i][j].has_bottom_wall = False
            # LEFT
            if dir[0] == i-1:
                self.__cells[i][j].has_left_wall = False
            # RIGHT
            if dir[0] == i+1:
                self.__cells[i][j].has_right_wall = False

            self.__draw_cell(i, j)
            self.__break_walls_r(dir[0], dir[1])

    def __reset_cells_visited(self):
        for arr in self.__cells:
            for cell in arr:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self.__cells[i][j].visited = True
        if self.__cells[i][j] is self.__cells[-1][-1]:
            return True
        
        # UP
        if j - 1 >= 0 and self.__cells[i][j].has_top_wall == self.__cells[i][j-1].visited == False:
            self.__cells[i][j].draw_move(self.__cells[i][j-1])
            if self._solve_r(i, j-1) == True:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j-1], undo=True)
        # RIGHT
        if i + 1 < self.__num_cols and self.__cells[i][j].has_right_wall == self.__cells[i+1][j].visited == False:
            self.__cells[i][j].draw_move(self.__cells[i+1][j])
            if self._solve_r(i+1, j) == True:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i+1][j], undo=True)
        # DOWN
        if j + 1 < self.__num_rows and self.__cells[i][j].has_bottom_wall == self.__cells[i][j+1].visited == False:
            self.__cells[i][j].draw_move(self.__cells[i][j+1])
            if self._solve_r(i, j+1) == True:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j+1], undo=True)
        # LEFT
        if i - 1 >= 0 and self.__cells[i][j].has_left_wall == self.__cells[i-1][j].visited == False:
            self.__cells[i][j].draw_move(self.__cells[i-1][j])
            if self._solve_r(i-1, j) == True:
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i-1][j], undo=True)
        

        return False