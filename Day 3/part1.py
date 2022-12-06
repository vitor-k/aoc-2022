import string

def main():
    priority = 0
    with open("input.txt") as fp:
        for line in fp.readlines():
            line = line.strip()
            comp1 = set(line[:len(line)//2])
            comp2 = set(line[len(line)//2:])
            intersect = comp1 & comp2
            el = next(iter(intersect))
            if(el in string.ascii_lowercase):
                priority += ord(el)-ord('a')+1
            elif(el in string.ascii_uppercase):
                priority += ord(el)-ord('A')+27

    print(priority)

if __name__ == "__main__":
    main()