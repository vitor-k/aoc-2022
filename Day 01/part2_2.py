def main():
    elf = []
    max_cals = []

    with open("input.txt") as fp:
        while line := fp.readline():
            if line == "\n":
                cals = sum(elf)
                elf = []
                if len(max_cals) < 3 or cals > max_cals[2]:
                    max_cals.append(cals)
                    max_cals = sorted(max_cals, reverse=True)[:3]
            else:
                elf.append(int(line.strip()))
    
    print("Part 1: {}", max_cals[0])
    print("Part 2: {}", sum(max_cals))

if __name__ == "__main__":
    main()