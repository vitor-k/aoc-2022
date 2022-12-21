import re

def monkeyEval(numeric, m1, op, m2):
    match(op):
        case "+":
            result = numeric[m1] + numeric[m2]
        case "-":
            result = numeric[m1] - numeric[m2]
        case "*":
            result = numeric[m1] * numeric[m2]
        case "/":
            result = numeric[m1] / numeric[m2]
    return result

def main(filename):
    numeric = {}
    remaining = []
    with open(filename) as fp:
        for line in fp.readlines():
            monkey, value = line.split(":")
            if(value.strip().isnumeric()):
                numeric[monkey] = int(value)
            else:
                m1, op, m2 = re.match(r"(\w{4}) ([-+*/]) (\w{4})", value.strip()).groups()
                if(m1 in numeric and m2 in numeric):
                    numeric[monkey] = monkeyEval(numeric, m1, op, m2)
                else:
                    remaining.append((monkey, m1,op,m2))

    while(len(remaining)):
        for quad in remaining:
            monkey, m1, op, m2 = quad
            if(m1 in numeric and m2 in numeric):
                numeric[monkey] = monkeyEval(numeric, m1, op, m2)
                remaining.remove(quad)
                break

    print(numeric)
    print(numeric["root"])

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
