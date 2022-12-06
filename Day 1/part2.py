def main():
    data = []
    elf = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            if line == "\n":
                data.append(elf)
                elf = []
            else:
                elf.append(int(line.strip()))

    max_cals = []
    for elf in data:
        cals = sum(elf)
        if len(max_cals) < 3 or cals > max_cals[2]:
            max_cals.append(cals)
            max_cals = sorted(max_cals, reverse=True)[:3]
            
    print(sum(max_cals))

if __name__ == "__main__":
    main()