
def main():
    trees = []
    scenTrees = []
    with open("input.txt") as fp:
        for line in fp.readlines():
            trees.append([int(x) for x in line.strip()])
            scenTrees.append([0 for x in line.strip()])

    for i in range(len(trees)):
        for j in range(len(trees[0])):
            scenic = 1
            #from the top
            for k in reversed(range(i)):
                if(trees[k][j] >= trees[i][j]):
                    scenic *= i-k
                    break
            else:
                scenic *= i
            #from the left
            for k in reversed(range(j)):
                if(trees[i][k] >= trees[i][j]):
                    scenic *= j-k
                    break
            else:
                scenic *= j
            #from the bottom
            for k in range(i+1, len(trees)):
                if(trees[k][j] >= trees[i][j]):
                    scenic *= k-i
                    break
            else:
                scenic *= len(trees) - i - 1
            #from the right
            for k in range(j+1, len(trees[0])):
                if(trees[i][k] >= trees[i][j]):
                    scenic *= k-j
                    break
            else:
                scenic *= len(trees[0]) - j - 1
            scenTrees[i][j] = scenic

    print(scenTrees)
    print(max([max(line) for line in scenTrees]))

if __name__ == "__main__":
    main()