
def SNAFU2dec(input):
    output = 0
    for ch in input:
        match ch:
            case '-':
                output -= 1
            case '=':
                output -= 2
            case _:
                output += int(ch)
        output *= 5

    return output//5

def dec2SNAFU(input):
    output = ''

    while input > 0:
        match d := ((2 + input) % 5) - 2:
            case -1:
                output += '-'
            case -2:
                output += '='
            case _:
                output += str(d)
        input = (input - d) // 5

    return output[::-1]

def main(filename):
    numeric = []
    with open(filename) as fp:
        for line in fp.readlines():
            numeric.append(SNAFU2dec(line.strip()))
    
    print(sum(numeric))
    print(dec2SNAFU(sum(numeric)))

if __name__ == "__main__":
    filename = "example.txt"
    filename = "input.txt"
    main(filename)
