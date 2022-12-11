
class Monkey:
    Monkeys = []
    MonkMod = 1
    def __init__(self, items, op, test, truthy, falsy):
        self.items = items
        self.op = op
        self.test = test
        self.truthy = truthy
        self.falsy = falsy
        self.inspect = 0

        Monkey.Monkeys.append(self)
        Monkey.MonkMod *= self.test
    
    def turn(self):
        for item in self.items:
            old = item
            new = eval(self.op)
            new = new % Monkey.MonkMod
            self.inspect += 1
            testResult = new % self.test == 0
            if(testResult):
                self.throw(new,Monkey.Monkeys[self.truthy])
            else:
                self.throw(new,Monkey.Monkeys[self.falsy])
        self.items = []

    def throw(self, item, other):
        other.items.append(item)

    def __lt__(self,other):
        return self.inspect < other.inspect

def main(filename):
    monks = []
    with open(filename) as fp:
        lines = fp.readlines()
        i=0
        while(i < len(lines)):
            n = int(lines[i].split(" ")[1].strip(":\n"))
            i += 1
            # items
            line = lines[i].split(":")[1].strip()
            items = [int(x.strip()) for x in line.split(", ") if len(x.strip()) > 0]
            i += 1
            # operation
            op = lines[i].split("=")[1].strip()
            i += 1
            # test
            test = int(lines[i].split("by")[1].strip())
            i += 1
            # if true
            truthy = int(lines[i].split("monkey")[1].strip())
            i += 1
            # if false
            falsy = int(lines[i].split("monkey")[1].strip())
            i += 1
            # newline
            i += 1
            print("Moneky ", n, " items: ", items, "operation: ", op, "test: ", test, truthy,falsy)
            monks.append(Monkey(items,op,test,truthy,falsy))
    
    for i in range(10000):
        if(i % 100 == 0):
            print(i // 100, "%")
        for monkey in monks:
            monkey.turn()
    sm = sorted(monks, reverse=True)
    print(sm[0].inspect * sm[1].inspect)

if __name__ == "__main__":
    #filename = "example.txt"
    filename = "input.txt"
    main(filename)
