import unittest
from mars_rover_technical_challenge import Rover

class TestMarsRover(unittest.TestCase):
    def test_whereAmI(self):
        machine_1 = Rover(5, 6, "N")
        assert machine_1.whereAmI() == (5, 6, "N")

    def test_whereAmICompareTrue(self):
        machine_1 = Rover(5, 6, "N")
        machine_3 = Rover(5, 6, "N")
        assert machine_1.whereAmI() == machine_3.whereAmI()

    def test_whereAmICompareFalse(self):
        machine_1 = Rover(5, 6, "N")
        machine_2 = Rover(0, 0, "W")
        assert machine_1.whereAmI() != machine_2.whereAmI()
    
    def test_turnLeft(self):
        machine_1 = Rover(5, 6, "N")
        machine_1.move("L")
        assert machine_1 == Rover(5, 6, "W")

    def test_turnRight(self):
        machine_1 = Rover(5, 6, "N")
        machine_1.move("R")
        assert machine_1 == Rover(5, 6, "E")

    def test_turnLeftTwoTimes(self):
        machine_1 = Rover(5, 6, "N")
        machine_1.move("L")
        machine_1.move("L")
        assert machine_1 == Rover(5, 6, "S")

    def test_turnRightTwoTimes(self):
        machine_1 = Rover(5, 6, "N")
        machine_1.move("R")
        machine_1.move("R")
        assert machine_1 == Rover(5, 6, "S")

    def test_turnLeftTwoTimes(self):
        machine_1 = Rover(5, 6, "E")
        machine_1.move("R")
        machine_1.move("R")
        assert machine_1 == Rover(5, 6, "W")

    def test_turnRightTwoTimes(self):
        machine_1 = Rover(5, 6, "N")
        machine_1.move("R")
        machine_1.move("R")
        assert machine_1 == Rover(5, 6, "S")

    def test_turnInBothDirections(self):
        machine_1 = Rover(5, 6, "E")
        machine_1.move("LRRLR")
        assert machine_1 == Rover(5, 6, "S")

    def test_moveHorizontaly(self):
        machine_1 = Rover(5, 6, "E")
        machine_1.move("M")
        assert machine_1 == Rover(6, 6, "E")

    def test_moveVerticaly(self):
        machine_1 = Rover(5, 6, "E")
        machine_1.move("M")
        assert machine_1 == Rover(6, 6, "E")

    def test_horizontalMapLimits(self):
        machine_2 = Rover(0, 0, "W")
        machine_2.move("M")
        assert machine_2 == Rover(0, 0, "W")

    def test_verticalMapLimits(self):
        machine_4 = Rover(5, 5, "E", 5, 5)
        machine_4.move("M")
        assert machine_4 == Rover(5, 5, "E")

    def test_combinedMovesRover1(self):
        machine_5 = Rover(1, 2, "N", 5, 5)
        machine_5.move("LMLMLMLMM")
        assert machine_5 == Rover(1, 3, "N")

    def test_combinedMovesRover2(self):
        machine_6 = Rover(3, 3, "E", 5, 5)
        machine_6.move("MMRMMRMRRM")
        assert machine_6 == Rover(5, 1, "E")