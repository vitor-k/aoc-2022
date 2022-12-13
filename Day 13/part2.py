
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

class Packet:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return inOrder(self.value,other.value)

def main(filename):
    pack2 = Packet([[2]])
    pack6 = Packet([[6]])
    packets = [pack2,pack6]
    with open(filename) as fp:
        for line in fp.readlines():
            if(line.strip()):
                packets.append(Packet(eval(line.strip())))
    
    packets.sort()
    print((packets.index(pack2)+1) * (packets.index(pack6)+1))

    pass

if __name__ == "__main__":
    #filename = "example.txt"
    filename = "input.txt"
    main(filename)
