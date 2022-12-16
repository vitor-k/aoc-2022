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
    def __init__(self, name, _rate, neighbours):
        self.name = name
        self.rate = _rate
        self.neighbours = neighbours
        Node.nodes.add(self)
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
        return self.name + ": " + self.rate

def walkPath(node, n=30, remaining=None, score = 0, max_score = 0):
    if(n <= 1):
        return score
    if(remaining is None):
        remaining = set(node for node in Node.nodes if node.rate > 0)
    if(len(remaining) == 0):
        return score
    remaining_score = (n-1 if node in remaining else n-2)*sum([node.rate if node in remaining else 0 for node in Node.nodes])
    if(max_score - score > remaining_score):
        #give up
        return score
    if(node in remaining):
        # you can either open the valve or not
        maxval = score
        ordered_nodes = sorted([x for x in node.connections if x in remaining], reverse=True) + [x for x in node.connections if x not in remaining]
        for other in ordered_nodes:
            opened_score = score+(n-1)*node.rate
            maxval = max(maxval, walkPath(other, n-2, remaining - set([node]), opened_score, max([opened_score, max_score, maxval])))

            maxval = max(maxval, walkPath(other, n-1, remaining, score, max(maxval, max_score)))
        return maxval
    else:
        maxval = score
        ordered_nodes = sorted([x for x in node.connections if x in remaining], reverse=True) + [x for x in node.connections if x not in remaining]
        for other in ordered_nodes:
            maxval = max(maxval, walkPath(other, n-1, remaining, score, max(maxval, max_score)))
        return maxval

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
    
    print(walkPath(start))


if __name__ == "__main__":
    filename = "example.txt"
    #filename = "input.txt"
    main(filename)
