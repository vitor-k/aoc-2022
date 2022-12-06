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

    max_cals = 0
    for elf in data:
        cals = sum(elf)
        if(cals > max_cals):
            max_cals = cals
    print(max_cals)

if __name__ == "__main__":
    main()