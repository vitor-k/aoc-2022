
def main():
    visited = set()
    Rope = [[0,0] for x in range(10)]
    visited.add((0,0))
    with open("input.txt") as fp:
        for line in fp.readlines():
            direction, n = line.split(" ")
            n = int(n)
            for i in range(n):
                match direction:
                    case 'R':
                        Rope[0][0] += 1
                    case 'L':
                        Rope[0][0] -= 1
                    case 'U':
                        Rope[0][1] += 1
                    case 'D':
                        Rope[0][1] -= 1
                for j in range(1,10):
                    # move the rest of the rope
                    if(abs(Rope[j-1][0]-Rope[j][0]) > 1 or abs(Rope[j-1][1]-Rope[j][1]) > 1):
                        if(abs(Rope[j-1][0]-Rope[j][0]) >= 1 and abs(Rope[j-1][1]-Rope[j][1]) >= 1):
                            t0 = 1 if Rope[j-1][0] > Rope[j][0] else -1
                            t1 = 1 if Rope[j-1][1] > Rope[j][1] else -1
                            Rope[j][0]+= t0
                            Rope[j][1]+= t1
                            pass
                        elif abs(Rope[j-1][0]-Rope[j][0]) > 1:
                            t0 = 1 if Rope[j-1][0] > Rope[j][0] else -1
                            Rope[j][0]+= t0
                        else:
                            t1 = 1 if Rope[j-1][1] > Rope[j][1] else -1
                            Rope[j][1]+= t1
                        if(j==9):
                            visited.add((Rope[9][0], Rope[9][1]))
                        pass

    print(len(visited))

if __name__ == "__main__":
    main()