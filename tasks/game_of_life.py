class Life:
    def __init__(self, grid) -> None:
        self.grid = grid

    def getGrid(self):
        return self.grid
    
    def nextGeneration(self):
        check = self.grid.split("\n")
        for c, p in enumerate(check):
            check[c] = p.replace('.*.', '...')
        for c, p in enumerate(check):
            check[c] = p.replace('***', '.*.')
        self.grid = '\n'.join(check)
        return self.grid

def getNeighbors(index, line):
    return line[index - 1] + line[index + 1] 
