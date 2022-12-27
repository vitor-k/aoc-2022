
class Node:
    def __init__(self, x:int, y:int, z:int, steam:bool) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.steam = steam
        self.neighbours = []
    def checkConnect(self, other):
        manhattan = abs(self.x-other.x) + abs(self.y-other.y) + abs(self.z-other.z)
        if manhattan == 1 and other not in self.neighbours:
            self.neighbours.append(other)
    def exposedArea(self):
        return len([s for s in self.neighbours if s.steam])
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y and self.z == __o.z
    def __hash__(self) -> int:
        return hash((self.x,self.y,self.z))
    def __repr__(self) -> str:
        return "({}, {}, {})".format(self.x, self.y, self.z)

def floodFill(cubes):
    xvalues = [cube.x for cube in cubes]
    yvalues = [cube.y for cube in cubes]
    zvalues = [cube.z for cube in cubes]

    xmax = max(xvalues)+1
    xmin = min(xvalues)-1
    ymax = max(yvalues)+1
    ymin = min(yvalues)-1
    zmax = max(zvalues)+1
    zmin = min(zvalues)-1

    steam = set()

    for x in range(xmin,xmax+1):
        steam |= set([Node(x,y,zmax,True) for y in range(ymin,ymax+1)])
        steam |= set([Node(x,y,zmin,True) for y in range(ymin,ymax+1)])
    for y in range(ymin,ymax+1):
        steam |= set([Node(xmin,y,z,True) for z in range(zmin,zmax+1)])
        steam |= set([Node(xmax,y,z,True) for z in range(zmin,zmax+1)])
    for z in range(zmin,zmax+1):
        steam |= set([Node(x,ymin,z,True) for x in range(xmin,xmax+1)])
        steam |= set([Node(x,ymax,z,True) for x in range(xmin,xmax+1)])

    l = 0
    while len(steam) > l:
        l = len(steam)
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                for z in range(zmin, zmax):
                    s = Node(x,y,z,True)
                    if(s not in cubes and s not in steam):
                        for o in steam:
                            s.checkConnect(o)
                        if(len(s.neighbours) > 0):
                            steam.add(s)
    return steam

def main(filename):
    cubes = set()
    with open(filename) as fp:
        for line in fp.readlines():
            x,y,z = line.strip().split(',')
            cubes.add(Node(int(x),int(y),int(z),False))

    for cube in cubes:
        for other in cubes - set([cube]):
            cube.checkConnect(other)

    steam = floodFill(cubes)

    for cube in cubes:
        for s in steam:
            cube.checkConnect(s)

    print(sum([cube.exposedArea() for cube in cubes]))


if __name__ == "__main__":
    filename = "example.txt"
    #filename = "input.txt"
    main(filename)
