import string

def main():
    contained = 0
    with open("input.txt") as fp:
        for line in fp.readlines():
            (a,b) = line.split(',')
            a_low, a_high = [int(x) for x in a.split('-')]
            b_low, b_high = [int(x) for x in b.split('-')]
            if(a_high-a_low >= b_high - b_low):
                pass
                if(a_high >= b_high and a_low <= b_low):
                    contained += 1
            else:
                if(a_high <= b_high and a_low >= b_low):
                    contained += 1

            

    print(contained)

if __name__ == "__main__":
    main()