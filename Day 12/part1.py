
class Node:
    OpenSet = []
    def __init__(self, height, start=False, end=False):
        self.height = height
        self.connecteds = []
        self.start = start
        self.end = end
        if(start):
            self.n = 0
            Node.OpenSet.append(self)
        else:
            self.n = 2625
        self.done = False
    def defineStart(self):
        self.start = True
        self.n = 0
        Node.OpenSet.append(self)
    def addConnection(self, other):
        if(other.height - self.height <= 1):
            self.connecteds.append(other)
        if(self.height - other.height <= 1):
            other.connecteds.append(self)
    def djikstra(self):
        if(self.done):
            return
        if(self.end):
            print(self.n)
            return
        for node in self.connecteds:
            node.n = min(node.n, self.n+1)
        self.done = True
        for node in self.connecteds:
            if(not node.done):
                Node.OpenSet.append(node)
    def __lt__(self, other):
        return self.n < other.n

def main(filename):
    heightmap = []
    with open(filename) as fp:
        lines = fp.readlines()
        i = 0
        for i in range(len(lines)):
            line = lines[i]
            if(line.lower() != line):
                if(line.find("S") != -1):
                    start = (i,line.find("S"))
                    line = line.replace("S", "a")
                if(line.find("E") != -1):
                    epos = (i,line.find("E"))
                    line = line.replace("E", "z")
            heightmap.append([ord(x)-ord('a') for x in line.strip()])
    print(start)
    print(epos)

    print(len(heightmap)*len(heightmap[0]))
    
    mapgraph = [[Node(x) for x in line] for line in heightmap]
    mapgraph[start[0]][start[1]].defineStart()
    mapgraph[epos[0]][epos[1]].end = True
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if(i>0):
                mapgraph[i][j].addConnection(mapgraph[i-1][j])
            if(j>0):
                mapgraph[i][j].addConnection(mapgraph[i][j-1])

    while(len(Node.OpenSet) > 0):
        Node.OpenSet.sort(reverse=True)
        node = Node.OpenSet.pop()
        node.djikstra()

if __name__ == "__main__":
    filename = "example.txt"
    #filename = "input.txt"
    main(filename)
