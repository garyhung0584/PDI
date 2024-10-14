try:
    r1p1 = int(input())
    if r1p1 != 10:
        r1p2 = int(input())
        if r1p1 + r1p2 > 10 or r1p2 > 10 or r1p2 < 0:
            exit()

    r2p1 = int(input())
    if r2p1 != 10:
        r2p2 = int(input())
        if r2p1 + r2p2 > 10 or r2p2 > 10 or r2p2 < 0:
            exit()

    r3p1 = int(input())
    if r3p1 != 10:
        r3p2 = int(input())
        if r3p1 + r3p2 > 10 or r3p2 > 10 or r3p2 < 0:
            exit()

        if r3p1 + r3p2 == 10:
            bonus1 = int(input())
    else:
        bonus1 = int(input())
        bonus2 = int(input())
except:
    exit()

if r1p1 < 0 or r1p1 > 10 or r2p1 < 0 or r2p1 > 10 or r3p1 < 0 or r3p1 > 10:
    exit()


def calculateScore():
    score = 0
    if r1p1 == 10:
        score += 10
        if r2p1 == 10:
            score += r2p1 + r2p1
            if r3p1 == 10:
                score += r3p1 + r3p1 + r3p1
                score += bonus1 * 2
                score += bonus2
            else:
                score += r3p1 * 3
                score += r3p2 * 2
                if r3p1 + r3p2 == 10:
                    score += bonus1
        else:
            score += r2p1 * 2
            score += r2p2 * 2
            if r2p1 + r2p2 == 10:
                score += r3p1
            if r3p1 == 10:
                score += 10
                score += bonus1
                score += bonus2
            else:
                score += r3p1
                score += r3p2
                if r3p1 + r3p2 == 10:
                    score += bonus1
    else:
        score += r1p1
        score += r1p2
        if r1p1 + r1p2 == 10:
            score += r2p1
        if r2p1 == 10:
            score += 10
            if r3p1 == 10:
                score += r3p1 + r3p1
                score += bonus1 * 2
                score += bonus2
            else:
                score += r3p1 * 2
                score += r3p2 * 2
                if r3p1 + r3p2 == 10:
                    score += bonus1
        else:
            score += r2p1
            score += r2p2
            if r2p1 + r2p2 == 10:
                score += r3p1
            if r3p1 == 10:
                score += 10
                score += bonus1
                score += bonus2
            else:
                score += r3p1
                score += r3p2
                if r3p1 + r3p2 == 10:
                    score += bonus1
    print(score)


calculateScore()
