
def main():
    trees = []
    visTrees = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            trees.append([int(x) for x in line.strip()])
            visTrees.append([False for x in line.strip()])

    for i in range(len(trees)):
        visTrees[i][0] = True
        visTrees[i][-1] = True
    for j in range(len(trees[0])):
        visTrees[0][j] = True
        visTrees[-1][j] = True

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            #from the top
            for k in reversed(range(i)):
                if(trees[k][j] >= trees[i][j]):
                    break
            else:
                visTrees[i][j] = True
            #from the left
            for k in reversed(range(j)):
                if(trees[i][k] >= trees[i][j]):
                    break
            else:
                visTrees[i][j] = True
            #from the bottom
            for k in range(i+1, len(trees)):
                if(trees[k][j] >= trees[i][j]):
                    break
            else:
                visTrees[i][j] = True
            #from the right
            for k in range(j+1, len(trees[0])):
                if(trees[i][k] >= trees[i][j]):
                    break
            else:
                visTrees[i][j] = True

    print(sum([line.count(True) for line in visTrees]))

if __name__ == "__main__":
    main()