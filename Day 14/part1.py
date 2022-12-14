
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
        #print(list(range(min(p1[1],p2[1]),1+max(p1[1],p2[1]))))
        return [Block(p1[0], y) for y in range(min(p1[1],p2[1]),1+max(p1[1],p2[1]))]
    else:
        # horizontal path
        #print(list(range(min(p1[0],p2[0]),1+max(p1[0],p2[0]))))
        return [Block(x, p1[1]) for x in range(min(p1[0],p2[0]),1+max(p1[0],p2[0]))]

def checkIntercept(piles, rocks, p):
    for block in sorted(piles | rocks):
        if(block.intercept(p)):
            return block
    return None

def fall(piles, rocks, p):
    maxy = max([rock.y for rock in rocks])
    while(p.y < maxy):
        while(p not in piles | rocks):
            p.y += 1
            if(p.y > maxy):
                return None
        p.x = p.x-1
        if(p in piles | rocks):
            p.x = p.x+2
            if(p in piles | rocks):
                p.x = p.x-1
                p.y = p.y - 1
                return p


def main(filename):
    rocks = []
    with open(filename) as fp:
        for line in fp.readlines():
            pathline = line.split("->")
            pathline = list([x.strip() for x in pathline])
            #print(pathline)
            blockline = [pathToBlock(pathline[i],pathline[i+1]) for i in range(len(pathline)-1)]
            for block in blockline:
                rocks.extend(block)
    rocks = set(rocks)
    maxy = max([rock.y for rock in rocks])
    #print(rocks)
    #print(sorted(rocks))
    sand_piles = set()
    voidfalls = False
    while not voidfalls:
        p = Block(500,0)
        voidfalls = True
        # while(checkIntercept(sand_piles,rocks, p) is not None):
        #     pile = checkIntercept(sand_piles, rocks, p)
        #     #print(pile)
        #     tmp = Block(pile.x-1,pile.y)
        #     if(tmp not in sand_piles | rocks):
        #         p.x = tmp.x
        #         p.y = tmp.y
        #     else:
        #         tmp.x = pile.x + 1
        #         if(tmp not in sand_piles | rocks):
        #             p.x = tmp.x
        #             p.y = tmp.y
        #         else:
        #             voidfalls = False
        #             p.x = pile.x
        #             p.y = pile.y - 1
        #             sand_piles.add(p)
        #             #print(p)
        #             break
        tmp = fall(sand_piles, rocks, p)
        if(tmp is not None):
            voidfalls = False
            sand_piles.add(tmp)

    print(len(sand_piles))
    

if __name__ == "__main__":
    #filename = "example.txt"
    filename = "input.txt"
    main(filename)
