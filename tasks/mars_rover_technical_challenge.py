class Rover:
    def __init__(self, x, y, d, mx = 100, my = 100) -> None:
        self.mx = mx
        self.my = my
        self.x = x
        self.y = y
        self.d = d

    def __repr__(self) -> str:
        return self.whereAmI().__repr__()
    
    def __eq__(self, __value) -> bool:
        return self.whereAmI() == __value.whereAmI()

    def whereAmI(self):
        return (self.x, self.y, self.d)
    
    def move(self, input):
        move = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
        left = {"N": "W", "S": "E", "W": "S", "E": "N"}
        for cmd in [*input]:
            if cmd == "L":
                self.d = left[self.d]
            elif cmd == "R":
                if self.d == "E":
                    self.d = "S"
                elif self.d == "S":
                    self.d = "W"
                elif self.d == "W":
                    self.d = "N"
                else:
                    self.d = "E"
            elif cmd == "M":
                newx = self.x + move[self.d][0]
                newy = self.y + move[self.d][1]
                if newx >= 0 and newx <= self.mx:
                    self.x = newx
                if newy >= 0 and newy <= self.my:
                    self.y = newy

"""                 if self.d == "W" and self.x > 0:
                    self.x -= 1
                elif self.d == "E" and self.x < self.mx:
                    self.x += 1
                elif self.d == "N" and self.y < self.my:
                    self.y += 1
                elif self.d == "S" and self.y > 0:
                    self.y -= 1 """

machine_1 = Rover(5, 6, "N")
machine_2 = Rover(0, 0, "W")
machine_3 = Rover(5, 6, "N")
machine_4 = Rover(5, 5, "E", 5, 5)

""" def object_play():
    print(machine_1.whereAmI())
    print(machine_1.d) Hack

    print(machine_1)
    print(machine_1 == machine_1)
    print(machine_2 == machine_1)
    print(machine_3 == machine_1)
 """
def test():
    machine_1.move("L")
    assert machine_1 == Rover(5, 6, "W")
    machine_1.move("L")
    assert machine_1 == Rover(5, 6, "S")
    machine_1.move("L")
    machine_1.move("L")
    assert machine_1 == Rover(5, 6, "N")
    machine_1.move("R")
    assert machine_1 == Rover(5, 6, "E")
    machine_1.move("R")
    assert machine_1 == Rover(5, 6, "S")
    machine_1.move("R")
    assert machine_1 == Rover(5, 6, "W")
    machine_1.move("R")
    assert machine_1 == Rover(5, 6, "N")
    machine_1.move("R")
    assert machine_1 == Rover(5, 6, "E")
    machine_1.move("R")
    machine_1.move("R")
    assert machine_1 == Rover(5, 6, "W")
    machine_1.move("W")
    assert machine_1 == Rover(5, 6, "W")
    machine_1.move("M")
    assert machine_1 == Rover(4, 6, "W")
    machine_1.move("R")
    machine_1.move("R")
    machine_1.move("M")
    assert machine_1 == Rover(5, 6, "E")
    machine_2.move("M")
    assert machine_2 == Rover(0, 0, "W")
    machine_4.move("M")
    assert machine_4 == Rover(5, 5, "E")
    machine_4.move("L")
    machine_4.move("M")
    assert machine_4 == Rover(5, 5, "N")
    machine_2.move("L")
    machine_2.move("M")
    assert machine_2 == Rover(0, 0, "S")
    machine_5 = Rover(1, 2, "N", 5, 5)
    machine_5.move("LMLMLMLMM")
    assert machine_5 == Rover(1, 3, "N")
    machine_6 = Rover(3, 3, "E", 5, 5)
    machine_6.move("MMRMMRMRRM")
    assert machine_6 == Rover(5, 1, "E")

if __name__ == '__main__':
    test()