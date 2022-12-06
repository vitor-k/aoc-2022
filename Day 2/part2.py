def main():
    score = []
    decrypt = {"A":0, "B":1, "C":2, "X":-1, "Y":0, "Z":1}
    with open("input.txt") as fp:
        for line in fp.readlines():
            moves = line.split()
            opponent = decrypt[moves[0]]
            yours = 1 + ((opponent-1) + decrypt[moves[1]]) % 3
            outcome = 1
            if (yours-opponent) % 3 == 1:
                #win
                outcome += 6
                pass
            elif yours == opponent:
                #draw
                outcome += 3
                pass
            else:
                #lose
                pass
            score.append(outcome+yours)

    print(sum(score))

if __name__ == "__main__":
    main()