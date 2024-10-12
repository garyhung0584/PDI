r1p1 = int(input())
if r1p1 != 10:
    r1p2 = int(input())
r2p1 = int(input())
if r2p1 != 10:
    r2p2 = int(input())
r3p1 = int(input())
if r3p1 != 10:
    r3p2 = int(input())
    if r3p1 + r3p2 == 10:
        bonus1 = int(input())
if r3p1 == 10:
    bonus1 = int(input())
    bonus2 = int(input())


def calculateScore():
    score = 0
    if r1p1 == 10:
        score += 10
        if r2p1 == 10:
            score += 20
            if r3p1 == 10:
                score += 30
                score += bonus1
                score += bonus2
            else:
                score += r3p1
                score += r3p2
        else:
            score += r2p1 * 2
            score += r2p2 * 2
    else:
        score += r1p1
        score += r1p2
        if r1p1 + r1p2 == 10:
            score += r2p1


print(calculateScore())
