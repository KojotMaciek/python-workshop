import unittest
import game_of_life

class TestGameOfLife(unittest.TestCase):
    def test_classExist(self):
        l = game_of_life.Life("0 0")

    def test_getGrid(self):
        l = game_of_life.Life("0 0")
        assert l.getGrid() == "0 0"

    def test_generateLife(self):
        l = game_of_life.Life("0 0")
        l.nextGeneration()
        assert l.getGrid() == "0 0"

    def test_lastCellDies(self):
        l = game_of_life.Life("3 3\n...\n.*.\n...")
        l.nextGeneration()
        assert l.getGrid() == "3 3\n...\n...\n..."

    def test_lastCellLives(self):
        l = game_of_life.Life("3 5\n.....\n.***.\n.....")
        l.nextGeneration()
        assert l.getGrid() == "3 5\n.....\n..*..\n....."
