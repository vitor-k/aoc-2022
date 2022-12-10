
def main(filename):
    RegisterX = 1
    cycle = 1
    crt = [40*[0] for x in range(6)]
    with open(filename) as fp:
        for line in fp.readlines():
            noop = False
            n = 0
            if(line.strip() == "noop"):
                noop = True
            else:
                _, n = line.split(" ")
                n = int(n)
            if(abs((cycle-1)%40 - RegisterX) <= 1):
                crt[cycle//40][(cycle-1)%40] = 1
            cycle += 1
            if(not noop):
                if(abs((cycle-1)%40 - RegisterX) <= 1):
                    crt[cycle//40][(cycle-1)%40] = 1
                RegisterX += n
                cycle += 1

    for line in crt:
        print("".join(['#' if x==1 else '.' for x in line]))

if __name__ == "__main__":
    #filename = "example.txt"
    #filename = "exampleLarge.txt"
    filename = "input.txt"
    main(filename)
