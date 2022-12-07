class Node:
    def __init__(self, parent = None) -> None:
        self.children = {}
        self.parent = parent
        self.size = 0
    def getSize(self) -> int:
        if(len(self.children) == 0):
            #leaf
            return self.size
        else:
            total_size = 0
            for key in self.children:
                total_size += self.children[key].getSize()
            return total_size + self.size
    def computeSize(self,tally) -> None:
        for key in self.children:
            if(self.children[key].getSize() <= 100000):
                tally.append(self.children[key].getSize())
            self.children[key].computeSize(tally)
        
def main():
    folders = Node()
    cwd = folders
    with open("input.txt") as fp:
        for line in fp.readlines():
            if line.startswith("$ cd") :
                if(line.removeprefix("$ cd ").strip() == "/"):
                    cwd = folders
                elif(line.removeprefix("$ cd ").strip() == ".."):
                    # move up one level
                    cwd = cwd.parent
                else:
                    cwd = cwd.children[line.removeprefix("$ cd ").strip()]
            elif line.startswith("$ ls") :
                pass
            else:
                if(line.startswith("dir")):
                    cwd.children[line.removeprefix("dir ").strip()] = Node(cwd)
                else:
                    cwd.size += int(line.split(" ")[0])

    tally = []
    folders.computeSize(tally)
    print(sum(tally))

if __name__ == "__main__":
    main()