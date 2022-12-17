
def main():
    visited = set()
    H = (0,0)
    T = (0,0)
    visited.add((0,0))
    with open("input.txt") as fp:
        for line in fp.readlines():
            direction, n = line.split(" ")
            n = int(n)
            for i in range(n):
                match direction:
                    case 'R':
                        H = (H[0]+1, H[1])
                    case 'L':
                        H = (H[0]-1, H[1])
                    case 'U':
                        H = (H[0], H[1]+1)
                    case 'D':
                        H = (H[0], H[1]-1)
                if(abs(H[0]-T[0]) > 1 or abs(H[1]-T[1]) > 1):
                    # move tail
                    if((abs(H[0]-T[0]) >= 1 and abs(H[1]-T[1]) >= 1)):
                        t0 = 1 if H[0] > T[0] else -1
                        t1 = 1 if H[1] > T[1] else -1
                        T = (T[0]+t0,T[1]+t1)
                        pass
                    elif abs(H[0]-T[0]) > 1:
                        t0 = 1 if H[0] > T[0] else -1
                        T = (T[0]+t0,T[1])
                    else:
                        t1 = 1 if H[1] > T[1] else -1
                        T = (T[0],T[1]+t1)
                    visited.add(T)
                    pass

    print(len(visited))

if __name__ == "__main__":
    main()