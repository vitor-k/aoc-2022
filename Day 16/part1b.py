import re

class Valve:
    def __init__(self, pressure) -> None:
        self.pressure = pressure
        self.n = 0
        pass
    def open(self, n):
        self.n = n
        return self.n * self.pressure
    def total(self):
        return self.n * self.pressure

class Node:
    nodes = set()
    OpenSet = []
    MaxVal = 31
    def __init__(self, name, _rate, neighbours):
        self.name = name
        self.rate = _rate
        self.neighbours = neighbours
        Node.nodes.add(self)
        self.n = Node.MaxVal
        self.done = False
        self.end = False
    @property
    def connections(self):
        return [o for o in Node.nodes if o.name in self.neighbours]
    def __lt__(self, other) -> bool:
        return self.rate < other.rate
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name
    def __repr__(self) -> str:
        return self.name + ": " + str(self.rate)
    def djikstra(self):
        if(self.done):
            return
        if(self.end):
            return
        for node in self.connections:
            node.n = min(node.n, self.n+1)
        self.done = True
        for node in self.connections:
            if(not node.done):
                Node.OpenSet.append(node)

def resetNodes():
    for node in Node.nodes:
        node.n = Node.MaxVal
        node.done = False
        node.end = False

def runDjikstra(start, end):
    resetNodes()
    start.n = 0
    end.end = True
    Node.OpenSet = [start]
    while(len(Node.OpenSet) > 0):
        Node.OpenSet.sort(reverse=True)
        node = Node.OpenSet.pop()
        node.djikstra()
    return end.n

def explore(start, nodes, nodeMap, __n=30, score=0, max_score=0):
    if(__n <= 0 or len(nodes)==0):
        return score
    remaining_score = __n*sum([node.rate for node in nodes])
    if(max_score-score > remaining_score):
        return score
    maxp = 0
    for node in sorted(nodes, reverse=True):
        tmp = max(__n-nodeMap[(start,node)]-1, 0)
        newscore = score+tmp*node.rate
        p = explore(node, nodes-set([node]), nodeMap, tmp, newscore, max_score=max(maxp,max_score))
        maxp = max(p, maxp)
    return maxp

def main(filename):
    start = None
    with open(filename) as fp:
        for line in fp.readlines():
            values = re.match(r"Valve (\w{2}) has flow rate=(-?\d+); tunnels? leads? to valves? ([\w, ]+)", line.strip())
            valve, rate, neighbours = values.groups()
            neighbours = neighbours.split(", ")
            
            node = Node(valve, int(rate), neighbours)
            if(valve == "AA"):
                start = node
    
    validNodes = set(node for node in Node.nodes if node.rate > 0)
    nodeMap = {}
    for node in validNodes:
        for other in validNodes - set([node]):
            nodeMap[(node,other)] = runDjikstra(node,other)
    for node in validNodes:
        nodeMap[(start,node)] = runDjikstra(start,node)

    print("Djikstra Done")

    print(explore(start,validNodes,nodeMap))

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
