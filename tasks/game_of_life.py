import re

class Life:
    def __init__(self, grid) -> None:
        self.grid = grid

    def getGrid(self):
        return self.grid
    
    def nextGeneration(self):
        old_generation = self.grid.split("\n")
        new_generation = old_generation.copy()
        for y in range(1, len(old_generation)):
            p = old_generation[y]
            new_line = "."
            for x in range(1, len(p)-1):
                if getNeighbors(x, y, old_generation) != "**":
                    new_line += "."
                else:
                    new_line += p[x]
            new_generation[y] = new_line + "."

        self.grid = '\n'.join(new_generation)
        return self.grid

def getNeighbors(x, y, grid):
    return grid[y][x - 1] + grid[y][x + 1] 
