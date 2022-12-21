
class Numbry:
    Original = []
    i = 0
    id = 0
    zero = None
    def __init__(self,n) -> None:
        self.n = n
        if(n==0):
            Numbry.zero = self
        self.id = Numbry.id
        Numbry.id += 1
        Numbry.Original.append(self)
        pass
    def next():
        if(Numbry.i >= len(Numbry.Original)):
            return None
        n = Numbry.Original[Numbry.i]
        Numbry.i += 1
        return n
    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id

def main(filename):
    mixed = []
    with open(filename) as fp:
        for line in fp.readlines():
            mixed.append(Numbry(int(line.strip())))

    while n := Numbry.next():
        if(n.n == 0):
            continue
        i = mixed.index(n)
        mixed.remove(n)
        mixed.insert((i+n.n)%len(mixed), n)

    i = mixed.index(Numbry.zero)
    l = len(mixed)
    print(sum([mixed[(i+1000)%l].n, mixed[(i+2000)%l].n, mixed[(i+3000)%l].n]))


if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
