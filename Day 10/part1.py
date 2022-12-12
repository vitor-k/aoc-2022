
def main(filename):
    RegisterX = 1
    cycle = 1
    signalStrength = []
    with open(filename) as fp:
        for line in fp.readlines():
            noop = False
            n = 0
            if(line.strip() == "noop"):
                noop = True
            else:
                _, n = line.split(" ")
                n = int(n)
            cycle += 1
            if((cycle+20) % 40 == 0):
                signalStrength.append(cycle*RegisterX)
            if(not noop):
                cycle += 1
                RegisterX += n
                if((cycle+20) % 40 == 0):
                    signalStrength.append(cycle*RegisterX)

    print(sum(signalStrength))

if __name__ == "__main__":
    #filename = "example.txt"
    #filename = "exampleLarge.txt"
    filename = "input.txt"
    main(filename)
