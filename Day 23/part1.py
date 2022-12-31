
from enum import Enum

class Direction(Enum):
    North = 0
    South = 1
    West = 2
    East = 3

class Node:
    nodes = []
    _Id = 0
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

        self.next_x = x
        self.next_y = y

        self.first_direction = Direction.North
        self._id = Node._Id
        Node._Id += 1
        Node.nodes.append(self)
    
    def findNode(x:int, y:int):
        for node in Node.nodes:
            if(node.x == x and node.y == y):
                return node
        return None
    def checkIntention(x:int, y:int):
        total = 0
        for node in Node.nodes:
            if(node.next_x == x and node.next_y == y):
                total += 1
        return total

    def update(self):
        self.x = self.next_x
        self.y = self.next_y
    def reset(self):
        self.next_x = self.x
        self.next_y = self.y

    def checkAround(self):
        if not Node.findNode(self.x, self.y-1) \
        and not Node.findNode(self.x-1, self.y-1) \
        and not Node.findNode(self.x+1, self.y-1) \
        and not Node.findNode(self.x, self.y+1) \
        and not Node.findNode(self.x-1, self.y+1) \
        and not Node.findNode(self.x+1, self.y+1) \
        and not Node.findNode(self.x-1, self.y) \
        and not Node.findNode(self.x+1, self.y):
            return True
        return False
    def checkNorth(self):
        if not Node.findNode(self.x, self.y-1) \
        and not Node.findNode(self.x-1, self.y-1) \
        and not Node.findNode(self.x+1, self.y-1):
            self.next_y = self.y - 1
            return True
        return False
    def checkSouth(self):
        if not Node.findNode(self.x, self.y+1) \
        and not Node.findNode(self.x-1, self.y+1) \
        and not Node.findNode(self.x+1, self.y+1):
            self.next_y = self.y + 1
            return True
        return False
    def checkWest(self):
        if not Node.findNode(self.x-1, self.y) \
        and not Node.findNode(self.x-1, self.y-1) \
        and not Node.findNode(self.x-1, self.y+1):
            self.next_x = self.x - 1
            return True
        return False
    def checkEast(self):
        if not Node.findNode(self.x+1, self.y) \
        and not Node.findNode(self.x+1, self.y-1) \
        and not Node.findNode(self.x+1, self.y+1):
            self.next_x = self.x + 1
            return True
        return False
    def step(self):
        if(self.checkAround()):
            self.reset()
            return
        d = self.first_direction
        for i in range(4):
            match d:
                case Direction.North:
                    if self.checkNorth():
                        return
                case Direction.South:
                    if self.checkSouth():
                        return
                case Direction.West:
                    if self.checkWest():
                        return
                case Direction.East:
                    if self.checkEast():
                        return
            d = Direction((d.value+1)%4)
        pass

    def __hash__(self) -> int:
        return hash(self._id)
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)

def firstHalf():
    for elf in Node.nodes:
        elf.step()

def secondHalf():
    for elf in Node.nodes:
        if Node.checkIntention(elf.next_x, elf.next_y) == 1:
            elf.update()
    for elf in Node.nodes:
        elf.first_direction = Direction((elf.first_direction.value+1)%4)
        elf.reset()

def printElves(elves):
    xvalues = [elf.x for elf in elves]
    yvalues = [elf.y for elf in elves]
    for y in range(min(yvalues),max(yvalues)+1):
        line = "".join(['#' if Node.findNode(x,y) else '.' for x in range(min(xvalues), max(xvalues)+1)])
        print(line)
    print()

def main(filename):
    elves = set()
    with open(filename) as fp:
        i = 0
        for line in fp.readlines():
            line = line.strip()
            for j in range(len(line)):
                if line[j] == '#':
                    elves.add(Node(j,i))
                pass
            i+=1

    #print(elves)
    for i in range(10):
        firstHalf()
        secondHalf()

        #print("Round ", i)
        #printElves(elves)

    xvalues = [elf.x for elf in elves]
    yvalues = [elf.y for elf in elves]

    print( (1 + max(xvalues) - min(xvalues)) * (1 + max(yvalues) - min(yvalues)) - len(elves))

if __name__ == "__main__":
    filename = "smallExample.txt"
    filename = "example.txt"
    #filename = "input.txt"
    main(filename)
