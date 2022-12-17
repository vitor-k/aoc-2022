
def main():
    with open("input.txt") as fp:
        for line in fp.readlines():
            # one line only
            for i in range(len(line)-13):
                fourteenchar = line[i:i+14]
                if(len(set(fourteenchar)) == 14):
                    print(i+14)
                    break


if __name__ == "__main__":
    main()