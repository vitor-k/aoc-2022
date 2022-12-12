
class Node:
    OpenSet = []
    MaxVal = 0
    def __init__(self, height, end=False):
        self.height = height
        self.connections = []
        self.end = end
        if(height == 0):
            self.n = 0
            Node.OpenSet.append(self)
        else:
            self.n = Node.MaxVal
        self.done = False
    def addConnection(self, other):
        if(other.height - self.height <= 1):
            self.connections.append(other)
        if(self.height - other.height <= 1):
            other.connections.append(self)
    def djikstra(self):
        if(self.done):
            return
        if(self.end):
            print(self.n)
            return
        for node in self.connections:
            node.n = min(node.n, self.n+1)
        self.done = True
        for node in self.connections:
            if(not node.done):
                Node.OpenSet.append(node)
    def __lt__(self, other):
        return self.n < other.n

def main(filename):
    heightmap = []
    with open(filename) as fp:
        lines = fp.readlines()
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

    Node.MaxVal = len(heightmap)*len(heightmap[0]) + 1
    
    mapgraph = [[Node(x) for x in line] for line in heightmap]
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
    #filename = "example.txt"
    filename = "input.txt"
    main(filename)
