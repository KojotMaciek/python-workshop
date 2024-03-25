import unittest
import game_of_life

class TestGameOfLife(unittest.TestCase):
    def test_classExist(self):
        l = game_of_life.Life("0 0")
        print('Testing basic functionality')

    def test_getGrid(self):
        l = game_of_life.Life("0 0")
        print('Testing \"0 0\"')
        assert l.getGrid() == "0 0"

    def test_generateLife(self):
        l = game_of_life.Life("0 0")
        l.nextGeneration()
        print('Testing generating life for grid \"0 0\"')
        assert l.getGrid() == "0 0"

    def test_lastCellDies(self):
        l = game_of_life.Life("3 3\n...\n.*.\n...")
        l.nextGeneration()
        print('Testing \"Last Cell Dies\" for grid \"3 3\"')
        assert l.getGrid() == "3 3\n...\n...\n..."

    def test_lastCellLives(self):
        l = game_of_life.Life("3 5\n.....\n.***.\n.....")
        l.nextGeneration()
        print('Testing \"Last Cell lives\" for grid \"3 5\"')
        assert l.getGrid() == "3 5\n.....\n..*..\n....."
    
    def test_lastTwoCellsDie(self):
        l = game_of_life.Life("3 5\n.....\n.*.*.\n.....")
        l.nextGeneration()
        print('Testing \"Last Cell lives\" for grid \"3 5\"')
        assert l.getGrid() == "3 5\n.....\n.....\n....."

    def test_lastTwoSiblingsDie(self):
        l = game_of_life.Life("3 5\n.....\n..**.\n.....")
        l.nextGeneration()
        print('Testing \"Last Cell lives\" for grid \"3 5\"')
        assert l.getGrid() == "3 5\n.....\n.....\n....."

    def test_verticalNeighbors(self):
        l = game_of_life.Life("4 5\n.....\n..**.\n..*..\n.....")
        l.nextGeneration()
        print('Testing \"Last Cell lives\" for grid \"4 5\"')
        assert l.getGrid() == "4 5\n.....\n..**.\n..**.\n....."
        l.nextGeneration()
        assert l.getGrid() == "4 5\n.....\n..**.\n..**.\n....."
    
    def test_finalCountdown(self):
        l = game_of_life.Life("4 8\n........\n....*...\n...**...\n........")
        l.nextGeneration()
        print('Testing \"Last Cell lives\" for grid \"4 5\"')
        assert l.getGrid() == "4 8\n........\n...**...\n...**...\n........"

    def test_blinker(self):
        blinker_pattern = "5 5\n.....\n.....\n.***.\n.....\n....."
        l = game_of_life.Life(blinker_pattern)
        l.nextGeneration()
        l.nextGeneration()
        print('Testing \"Last Cell lives\" for grid \"5 5\"')
        assert l.getGrid() == blinker_pattern

    def test_lifeConstructor(self):
        l = game_of_life.lifeConstructor(3, 3, [(1, 1)])
        assert l.getGrid() == "3 3\n...\n.*.\n..."
        l = game_of_life.lifeConstructor(4, 3, [(1, 1),(2, 1)])
        assert l.getGrid() == "4 3\n....\n.**.\n...."
