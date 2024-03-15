class Life:
    def __init__(self, grid) -> None:
        self.grid = grid

    def getGrid(self):
        return self.grid
    
    def nextGeneration(self):
        if self.grid.find(".*."):
            self.grid = self.grid.replace(".*.", "...")
        if self.grid.find("***"):
            self.grid = self.grid.replace("***", ".*.")