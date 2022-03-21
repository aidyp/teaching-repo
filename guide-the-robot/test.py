from src.robot import Robot
import unittest

DEFAULT_MAZE = [
    ["*", "*", "*", "x", "*"],
    ["*", "*", "*", ".", "*"],
    ["*", ".", ".", ".", "*"],
    ["*", ".", "*", "*", "*"],
    ["*", ".", "*", "*", "*"],
    ["*", "o", "*", "*", "*"]
]

class RoboTest(unittest.TestCase):

    def setUp(self) -> None:
        self.robot = Robot()
        self.robot.set_maze(DEFAULT_MAZE)

    
    def test_position_finding(self):
        self.assertEqual(self.robot.starting_pos, (5, 1))

    def test_position_ending(self):
        self.assertEqual(self.robot.ending_pos, (0, 3))

    def test_index_bounds(self):
        response = self.robot.move_down()
        self.assertEqual(response, "NO_PATH")

    def test_wall_bounds(self):
        response = self.robot.move_down()
        self.assertEqual(response, "NO_PATH")

    def test_open_space(self):
        pass