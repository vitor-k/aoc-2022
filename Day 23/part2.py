
from enum import Enum

class Direction(Enum):
    North = 0
    South = 1
    West = 2
    East = 3

class Node:
    nodes = []
    intentions = []
    roundMap = {}
    _Id = 0
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

        self.next_x = x
        self.next_y = y

        self.moved = False
        self.first_direction = Direction.North
        self._id = Node._Id
        Node._Id += 1
        Node.nodes.append(self)
        Node.roundMap[(x,y)] = self
    
    def findNode(x:int, y:int):
        return Node.roundMap[(x,y)] if (x,y) in Node.roundMap else None
    def checkIntention(x:int, y:int) -> int:
        return Node.intentions.count((x,y))

    def update(self):
        if(self.x != self.next_x or self.y != self.next_y):
            self.moved = True
        self.x = self.next_x
        self.y = self.next_y
    def reset(self):
        self.next_x = self.x
        self.next_y = self.y
        self.moved = False
        Node.roundMap[(self.x,self.y)] = self

    def checkAround(self) -> bool:
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
    def checkNorth(self) -> bool:
        if not Node.findNode(self.x, self.y-1) \
        and not Node.findNode(self.x-1, self.y-1) \
        and not Node.findNode(self.x+1, self.y-1):
            self.next_y = self.y - 1
            Node.intentions.append((self.next_x, self.next_y))
            return True
        return False
    def checkSouth(self) -> bool:
        if not Node.findNode(self.x, self.y+1) \
        and not Node.findNode(self.x-1, self.y+1) \
        and not Node.findNode(self.x+1, self.y+1):
            self.next_y = self.y + 1
            Node.intentions.append((self.next_x, self.next_y))
            return True
        return False
    def checkWest(self) -> bool:
        if not Node.findNode(self.x-1, self.y) \
        and not Node.findNode(self.x-1, self.y-1) \
        and not Node.findNode(self.x-1, self.y+1):
            self.next_x = self.x - 1
            Node.intentions.append((self.next_x, self.next_y))
            return True
        return False
    def checkEast(self) -> bool:
        if not Node.findNode(self.x+1, self.y) \
        and not Node.findNode(self.x+1, self.y-1) \
        and not Node.findNode(self.x+1, self.y+1):
            self.next_x = self.x + 1
            Node.intentions.append((self.next_x, self.next_y))
            return True
        return False
    def step(self):
        if(self.checkAround()):
            return
        d = self.first_direction
        match d:
            case Direction.North:
                if self.checkNorth():
                    return
                if self.checkSouth():
                    return
                if self.checkWest():
                    return
                if self.checkEast():
                    return
            case Direction.South:
                if self.checkSouth():
                    return
                if self.checkWest():
                    return
                if self.checkEast():
                    return
                if self.checkNorth():
                    return
            case Direction.West:
                if self.checkWest():
                    return
                if self.checkEast():
                    return
                if self.checkNorth():
                    return
                if self.checkSouth():
                    return
            case Direction.East:
                if self.checkEast():
                    return
                if self.checkNorth():
                    return
                if self.checkSouth():
                    return
                if self.checkWest():
                    return
        pass

    def __hash__(self) -> int:
        return hash(self._id)
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)

def bothHalves(round):
    for elf in Node.nodes:
        elf.step()

    for elf in Node.nodes:
        if Node.checkIntention(elf.next_x, elf.next_y) == 1:
            elf.update()
    if(len([elf for elf in Node.nodes if elf.moved]) == 0):
        print("Stopped at round {}!".format(round))
        return True
    Node.roundMap = {}
    for elf in Node.nodes:
        elf.first_direction = Direction((elf.first_direction.value+1)%4)
        elf.reset()
    Node.intentions = []
    return False

def main(filename):
    with open(filename) as fp:
        i = 0
        for line in fp.readlines():
            line = line.strip()
            for j in range(len(line)):
                if line[j] == '#':
                    Node(j,i)
                pass
            i+=1

    i=1
    while True:
        if(bothHalves(i)):
            break
        i+=1

if __name__ == "__main__":
    filename = "smallExample.txt"
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
