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

def letsPlay():
    try:
        grid_x = int(input("Enter the maximum width of the grid: "))
        grid_y = int(input("Enter the maximum height of the grid: "))
    except ValueError:
        print("Provided input is wrong. Enter an integer.")
    else: 
        coordinates = []
        message = "Enter x and y (example: 2, 2) and hit enter. To finish leave this form empty and hit enter: "
        counter = ((grid_x - 1) * (grid_y - 1))
        print("Give the coordinates of living cells:")
    
    try:
        format = "[1-9], [1-9]"
        while counter > 0:
            living_cell = input(message)
            if living_cell == "":
                break
            if not re.match(format, living_cell):
                raise TypeError
            counter -= 1
            coordinates.append(tuple(map(int, living_cell.split(', '))))
    except TypeError:
        print("Wrong format of the coordinates. Corrent form: x, y (example: 2, 2)")
    except Exception as error:
        print("An error occured", error)
    else:
        print("Your grid is: ")
        l = lifeConstructor(grid_x, grid_y, coordinates)
        for i in range(grid_x):
            print(l.getGrid())
            print("#" * grid_x)
            l.nextGeneration()
            time.sleep(0.5)
    finally:
        print("The game is over")

if __name__ == '__main__':
    with open('game_of_life.txt', 'r') as file:
        print(file.read())
    letsPlay()