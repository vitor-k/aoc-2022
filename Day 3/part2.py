import string

def main():
    priority = 0
    comp = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            comp.append(set(line.strip()))
            if(len(comp) == 3):
                intersect = comp[0] & comp[1] & comp[2]
                el = next(iter(intersect))
                if(el in string.ascii_lowercase):
                    priority += ord(el)-ord('a')+1
                elif(el in string.ascii_uppercase):
                    priority += ord(el)-ord('A')+27
                else:
                    print("Error: {}", comp)
                comp = []

    print(priority)

if __name__ == "__main__":
    main()