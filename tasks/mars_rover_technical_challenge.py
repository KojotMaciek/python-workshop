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
        right = {"N": "E", "S": "W", "W": "N", "E": "S"}
        for cmd in [*input]:
            if cmd == "L":
                self.d = left[self.d]
            elif cmd == "R":
                self.d = right[self.d]
            elif cmd == "M":
                newx = self.x + move[self.d][0]
                newy = self.y + move[self.d][1]
                if newx >= 0 and newx <= self.mx:
                    self.x = newx
                if newy >= 0 and newy <= self.my:
                    self.y = newy
