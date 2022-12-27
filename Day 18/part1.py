
class Node:
    def __init__(self, x:int, y:int, z:int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.neighbours = []
    def checkConnect(self, other):
        manhattan = abs(self.x-other.x) + abs(self.y-other.y) + abs(self.z-other.z)
        if manhattan == 1 and other not in self.neighbours:
            self.neighbours.append(other)
            if(self not in other.neighbours):
                other.neighbours.append(self)
    def exposedArea(self):
        return 6 - len(self.neighbours)

def main(filename):
    cubes = set()
    with open(filename) as fp:
        for line in fp.readlines():
            x,y,z = line.strip().split(',')
            cubes.add(Node(int(x),int(y),int(z)))

    for cube in cubes:
        for other in cubes - set([cube]):
            cube.checkConnect(other)

    print(sum([x.exposedArea() for x in cubes]))


if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
