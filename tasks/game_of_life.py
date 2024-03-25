import re
import time

class Life:
    def __init__(self, grid) -> None:
        self.grid = grid

    def getGrid(self):
        return self.grid
    
    def nextGeneration(self):
        old_generation = self.grid.split("\n")
        new_generation = old_generation.copy()
        for y in range(2, len(old_generation)-1):
            p = old_generation[y]
            new_line = "."
            for x in range(1, len(p)-1):
                neighbors =  getNeighbors(x, y, old_generation)
                if old_generation[y][x] == "." and countLiveNeighbors(neighbors) == 3:
                    new_line += "*"
                elif countLiveNeighbors(neighbors) not in [2, 3]:
                    new_line += "."
                else:
                    new_line += p[x]
            new_generation[y] = new_line + "."

        self.grid = '\n'.join(new_generation)
        return self.grid

def getNeighbors(x, y, grid):
    return grid[y + 1][(x - 1) : (x + 2)] + grid[y][x - 1] + grid[y][x + 1] + grid[y - 1][(x - 1) : (x + 2)]

def countLiveNeighbors(n):
    n = re.sub(r"[^*]", "", n)
    return len(n)

def lifeConstructor(max_x, max_y, pattern):
    grid = [str(max_x) + " " + str(max_y)]
    for iy in range(max_y):
        line = ""
        for ix in range(max_x):
            inserted = False
            for x, y in pattern:
                if ix == x and iy == y:
                    line += "*"
                    inserted = True
            if not inserted:
                line += "."
        grid.append(line)
    return Life('\n'.join(grid))

if __name__ == '__main__':
    l = lifeConstructor(50, 16, [(1, 1),(2, 2), (3, 2), (1, 3), (2, 3)])
    for i in range(40):
        print(l.getGrid())
        l.nextGeneration()
        time.sleep(0.5)