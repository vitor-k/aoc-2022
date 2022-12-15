import re

class Sensor:
    maxRadius = 0
    def __init__(self, sx,sy,bx,by):
        self.x = sx
        self.y = sy
        self.radius = abs(sx-bx) + abs(sy-by)
        Sensor.maxRadius = max(Sensor.maxRadius, self.radius)
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
    min_x = 0
    max_x = 0
    with open(filename) as fp:
        for line in fp.readlines():
            values = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line.strip())
            sx, sy, bx, by = (int(x) for x in values.groups())
            sensors.append(Sensor(sx,sy,bx,by))
            beacons.add(Beacon(bx,by))
            min_x = min([min_x, sx, bx])
            max_x = max([max_x, sx, bx])
    
    min_x = min_x - Sensor.maxRadius
    max_x = max_x + Sensor.maxRadius
    #target_y = 10
    target_y = 2000000
    n = 0
    for x in range(min_x, 1+max_x):
        inrange = False
        for sensor in sensors:
            if(sensor.inRange(x, target_y)):
                inrange = True
                break
        if(inrange):
            if(Beacon(x,target_y) in beacons):
            #    print("B", end='')
                pass
            else:
            #    print("#", end='')
                n+=1
        else:
            #print(".", end='')
            pass
    print("")
    print(n)
    pass    

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
