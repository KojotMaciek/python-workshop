class Rover:
    def __init__(self, x, y, d) -> None:
        self.x = x
        self.y = y
        self.d = d

    def __repr__(self) -> str:
        return self.whereAmI().__repr__()
    
    def __eq__(self, __value) -> bool:
        return self.whereAmI() == __value.whereAmI()

    def whereAmI(self):
        return (self.x, self.y, self.d)
    
    def move(self, cmd):
        if cmd == "L":
            if self.d == "N":
                self.d = "W"
            elif self.d == "S":
                self.d = "E"
            elif self.d == "W":
                self.d = "S"
            else:
                self.d = "N"
        elif cmd == "R":
            if self.d == "E":
                self.d = "S"
            elif self.d == "S":
                self.d = "W"
            elif self.d == "W":
                self.d = "N"
            else:
                self.d = "E"

machine_1 = Rover(5, 6, "N")
machine_2 = Rover(8, 9, "S")
machine_3 = Rover(5, 6, "N")

def object_play():
    print(machine_1.whereAmI())
    # print(machine_1.d) Hack

    print(machine_1)
    print(machine_1 == machine_1)
    print(machine_2 == machine_1)
    print(machine_3 == machine_1)

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

if __name__ == '__main__':
    test()