def main():
    score = []
    decrypt = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
    with open("input.txt") as fp:
        for line in fp.readlines():
            moves = line.split()
            opponent = decrypt[moves[0]]
            yours = decrypt[moves[1]]
            outcome = 0
            if (yours-opponent) % 3 == 1:
                #win
                outcome = 6
                pass
            elif yours == opponent:
                #draw
                outcome = 3
                pass
            else:
                #lose
                pass
            score.append(outcome+yours)

    print(sum(score))

if __name__ == "__main__":
    main()