import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_no_cells(self):
        m1 = Maze(0, 0, 0, 0, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            0,
        )

    def test_break_entrance_exit(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)

        # Entrance
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[0][0].has_left_wall,
            True
        )

        # Exit
        self.assertEqual(
            m1._Maze__cells[-1][-1].has_bottom_wall,
            False
        )
        self.assertEqual(
            m1._Maze__cells[-1][-1].has_right_wall,
            True
        )


if __name__ == "__main__":
    unittest.main()