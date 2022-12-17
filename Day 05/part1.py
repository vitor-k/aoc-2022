import string
import re

def main():
    tower = []
    first_time = True
    with open("input.txt") as fp:
        for line in fp.readlines():
            if(line[0] != 'm' and len(line.strip()) > 0):
                # crates
                n = (len(line))//4
                if(first_time):
                    tower = [[] for i in range(n)]
                    first_time = False
                for i in range(n):
                    tower[i].append(line[1+4*i])
            elif(line[0] == '\n'):
                # separator line
                for i in range(len(tower)):
                    tower[i] = [x for x in reversed(tower[i]) if x in string.ascii_letters]
                pass
            elif(line[0] == 'm'):
                # instructions
                instruction = re.match(r"move (\d+) from (\d+) to (\d+)", line)
                i, j, k = (int(x) for x in instruction.groups())
                
                for l in range(i):
                    el = tower[j-1].pop()
                    tower[k-1].append(el)
                
                pass



    print(''.join([t[-1] for t in tower]))

    pass

if __name__ == "__main__":
    main()