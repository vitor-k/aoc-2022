
def main():
    with open("input.txt") as fp:
        for line in fp.readlines():
            # one line only
            for i in range(len(line)-3):
                fourchar = line[i:i+4]
                if(len(set(fourchar)) == 4):
                    print(i+4)
                    break


if __name__ == "__main__":
    main()