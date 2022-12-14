
class Block:
    def __init__(self, x,y):
        self.x = x
        if(y < 0):
            print("Error!")
        self.y = y
    def intercept(self,other):
        if(other.x == self.x):
            if other.y <= self.y:
                return True
        return False
    def __lt__(self, other) -> bool:
        if(self.x == other.x):
            return self.y < other.y
        else:
            if(abs(self.x-500) == abs(other.x-500)):
                return self.x < other.x
            return abs(self.x-500) < abs(other.x-500)
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y
    def __hash__(self) -> int:
        return hash(tuple((self.x,self.y)))
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"
        pass

def pathToBlock(p1,p2):
    p1 = tuple(int(x) for x in p1.split(","))
    p2 = tuple(int(x) for x in p2.split(","))
    if(p1[0] == p2[0]):
        # vertical path
        return [Block(p1[0], y) for y in range(min(p1[1],p2[1]),1+max(p1[1],p2[1]))]
    else:
        # horizontal path
        return [Block(x, p1[1]) for x in range(min(p1[0],p2[0]),1+max(p1[0],p2[0]))]

def pathToHollow(p1,p2):
    p1 = tuple(int(x) for x in p1.split(","))
    p2 = tuple(int(x) for x in p2.split(","))
    if(p1[0] == p2[0]):
        # vertical path
        return []
    else:
        # horizontal path
        hollows = []
        length = abs(p1[0]-p2[0])
        for i in range(1,1+length//2):
            for j in range(min(p1[0],p2[0])+i,1+max(p1[0],p2[0])-i):
                hollows.append(Block(j,p1[1]+i))
        return hollows

def breedHollows(hollows, rocks, max_y):
    for hollow in hollows | rocks:
        left = Block(hollow.x-1, hollow.y)
        right = Block(hollow.x+1, hollow.y)
        if((left in hollows | rocks) and (right in hollows | rocks)):
            if(hollow.y+1 < max_y):
                tmp = Block(hollow.x, hollow.y+1)
                if(tmp not in hollows | rocks):
                    return tmp
    return None

def main(filename):
    rocks = []
    hollows = []
    with open(filename) as fp:
        for line in fp.readlines():
            pathline = line.split("->")
            pathline = list([x.strip() for x in pathline])
            #print(pathline)
            blockline = [pathToBlock(pathline[i],pathline[i+1]) for i in range(len(pathline)-1)]
            hollowline = [pathToHollow(pathline[i],pathline[i+1]) for i in range(len(pathline)-1)]
            for block in blockline:
                rocks.extend(block)
            for hollow in hollowline:
                hollows.extend(hollow)
    rocks = set(rocks)
    maxy = max([rock.y for rock in rocks])

    hollows = set([hollow for hollow in hollows if hollow.y < maxy+2 and hollow not in rocks])

    running = True
    while(running):
        tmp = breedHollows(hollows, rocks, maxy+2)
        if(tmp is None):
            running = False
        else:
            hollows.add(tmp)

    theorethical = (maxy+2)**2 - len(rocks | hollows)
    print(theorethical)

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
