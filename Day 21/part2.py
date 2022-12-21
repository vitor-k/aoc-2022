import re

class Monkey:
    numeric = {}
    remaining = {}
    def __init__(self, name, left = None, op = None, right = None, value = None) -> None:
        self.name = name
        self.left = left
        self.op = op
        self.right = right
        self.value = value
        if(value is not None):
            Monkey.numeric[self.name] = self.value
        else:
            Monkey.remaining[self.name] = self
    def eval(self):
        if(self.left in Monkey.numeric and self.right in Monkey.numeric):
            match(self.op):
                case "+":
                    result = Monkey.numeric[self.left] + Monkey.numeric[self.right]
                case "-":
                    result = Monkey.numeric[self.left] - Monkey.numeric[self.right]
                case "*":
                    result = Monkey.numeric[self.left] * Monkey.numeric[self.right]
                case "/":
                    result = Monkey.numeric[self.left] / Monkey.numeric[self.right]
            Monkey.numeric[self.name] = result
            del Monkey.remaining[self.name]
            return True
        else:
            return False
    def backtrack(self, value):
        if(self.name == "humn"):
            Monkey.numeric["humn"] = value
        if(self.eval()):
            return
        if(self.left in Monkey.numeric):
            match(self.op):
                case "+":
                    Monkey.remaining[self.right].backtrack(value - Monkey.numeric[self.left])
                case "-":
                    Monkey.remaining[self.right].backtrack(Monkey.numeric[self.left] - value)
                case "*":
                    Monkey.remaining[self.right].backtrack(value/Monkey.numeric[self.left])
                case "/":
                    Monkey.remaining[self.right].backtrack(Monkey.numeric[self.left]/value)
        if(self.right in Monkey.numeric):
            match(self.op):
                case "+":
                    Monkey.remaining[self.left].backtrack(value - Monkey.numeric[self.right])
                case "-":
                    Monkey.remaining[self.left].backtrack(value + Monkey.numeric[self.right])
                case "*":
                    Monkey.remaining[self.left].backtrack(value/Monkey.numeric[self.right])
                case "/":
                    Monkey.remaining[self.left].backtrack(value * Monkey.numeric[self.right])
    def __eq__(self, __o: str) -> bool:
        return self.name == __o
    def __repr__(self) -> str:
        return self.name + ": " + str(self.value)
def main(filename):
    root = None
    with open(filename) as fp:
        for line in fp.readlines():
            monkey, value = line.split(":")
            if(value.strip().isnumeric()):
                if(monkey == "humn"):
                    Monkey("humn")
                    continue
                Monkey(monkey, value=int(value))
            else:
                m1, op, m2 = re.match(r"(\w{4}) ([-+*/]) (\w{4})", value.strip()).groups()
                if(monkey == "root"):
                    root = (m1,m2)
                    continue
                Monkey(monkey, m1, op, m2)

    prev = len(Monkey.remaining)+1
    while(len(Monkey.remaining) < prev):
        prev = len(Monkey.remaining)
        for key in Monkey.remaining:
            if(Monkey.remaining[key].eval()):
                break

    if(root[1] in Monkey.numeric):
        Monkey.remaining[root[0]].backtrack(Monkey.numeric[root[1]])
    elif(root[0] in Monkey.numeric):
        Monkey.remaining[root[1]].backtrack(Monkey.numeric[root[0]])
    else:
        print("Error")

    print(Monkey.numeric["humn"])

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
