import re

class Sensor:
    def __init__(self, sx,sy,bx,by):
        self.x = sx
        self.y = sy
        self.radius = abs(sx-bx) + abs(sy-by)
    def distance(self, __x: int, __y: int) -> int:
        return abs(self.x - __x) + abs(self.y - __y)
    def inRange(self, __x: int, __y: int) -> bool:
        return self.distance(__x,__y) <= self.radius
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y
    def __hash__(self) -> int:
        return hash(tuple((self.x,self.y)))
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"
    def maxX(self, y):
        return self.x + (self.radius - abs(self.y - y))

class Beacon:
    def __init__(self, bx,by):
        self.x = bx
        self.y = by
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y
    def __hash__(self) -> int:
        return hash(tuple((self.x,self.y)))
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

def main(filename):
    sensors = []
    beacons = set()
    with open(filename) as fp:
        for line in fp.readlines():
            values = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line.strip())
            sx, sy, bx, by = (int(x) for x in values.groups())
            sensors.append(Sensor(sx,sy,bx,by))
            beacons.add(Beacon(bx,by))
    
    min_x = 0
    max_x = 4000000
    #max_x = 20
    min_y = 0
    max_y = 4000000
    #max_y = 20
    y = min_y
    while(y < max_y):
        x = min_x
        while(x < max_x):
            inrange = False
            rightmost_x = x
            for sensor in sensors:
                if(sensor.inRange(x, y)):
                    rightmost_x = max(rightmost_x, sensor.maxX(y))
                    inrange = True
                    break
            if(inrange):
                x = rightmost_x
            else:
                print(x,y)
                print(x*4000000 + y)
                pass
            x += 1
        y = y+1
    pass    

if __name__ == "__main__":
    #filename = "example.txt"
    filename = "input.txt"
    main(filename)
