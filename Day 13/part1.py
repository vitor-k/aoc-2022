
def inOrder(l,r):
    if type(l) is list and type(r) is list:
        for i in range(min(len(l),len(r))):
            if(inOrder(l[i],r[i])):
                return True
            elif(inOrder(r[i], l[i])):
                return False
        return len(l) < len(r)
    elif type(l) is int and type(r) is int:
        return l < r
    elif type(l) is list and type(r) is int:
        if(len(l) == 0):
            return True
        if(type(l[0]) is int):
            return l[0] < r
        return inOrder(l,[r])
    else:
        if(len(r) == 0):
            return False
        if(type(r[0]) is int):
            return l <= r[0]
        return inOrder([l],r)

def main(filename):
    in_order = 0
    with open(filename) as fp:
        lines = fp.readlines()
        i = 0
        while i < len(lines):
            line_l = lines[i].strip()
            i += 1
            line_r = lines[i].strip()
            i+=1
            #blankline
            i+=1
            l = eval(line_l)
            r = eval(line_r)
            orde = inOrder(l,r)
            if(orde):
                print(l,r)
            in_order += (i)//3 if inOrder(l,r) else 0
    print(in_order)

if __name__ == "__main__":
    #filename = "example.txt"
    filename = "input.txt"
    main(filename)
