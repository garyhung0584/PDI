PATTERN = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")
SUIT = ("C", "D", "H", "S")


def is_straight_flush(cards):
    return is_flush(cards) and is_straight(cards)


def is_four_of_a_kind(cards):
    num = [x[0] for x in cards]
    for i in num:
        if num.count(i) == 4:
            return True
    return False


def is_full_house(cards):
    num = [x[0] for x in cards]
    for i in num:
        if num.count(i) == 3:
            for j in num:
                if num.count(j) == 2:
                    return True
    return False


def is_flush(cards):
    return len(set([x[1] for x in cards])) == 1


def is_straight(cards):
    num = [x[0] for x in cards]
    num.sort()
    if num[0] == 1 and num[4] == 13:
        num = [x - 13 if x > 9 else x for x in num]
        num.sort()
    for i in range(1, 5):
        if num[i] - num[i - 1] != 1:
            return False
    return True


def is_three_of_a_kind(cards):
    num = [x[0] for x in cards]
    threeOfaKind = 0
    for i in num:
        if num.count(i) == 3:
            threeOfaKind += 1

    return True if threeOfaKind else False


def is_two_pairs(cards):
    num = [x[0] for x in cards]
    pairs = 0
    for i in num:
        if num.count(i) == 2:
            pairs += 1
    if pairs == 4:
        return True
    else:
        return False


def is_one_pair(cards):
    num = [x[0] for x in cards]
    pairs = 0
    for i in num:
        if num.count(i) == 2:
            pairs += 1
    if pairs:
        return True
    else:
        return False


def getCards():
    try:
        xCards = input().replace("10", "T").split()

        xCards = [
            (PATTERN.index(x[0]) + 1, SUIT.index(x[1])) if len(x) == 2 else 0
            for x in xCards
        ]

        if 0 in xCards:
            raise Exception
    except:
        print("Error input")
        exit()

    return xCards


def processResult(xCards):

    if is_straight_flush(xCards):
        print("9")
    elif is_four_of_a_kind(xCards):
        print("8")
    elif is_full_house(xCards):
        print("7")
    elif is_flush(xCards):
        print("6")
    elif is_straight(xCards):
        print("5")
    elif is_three_of_a_kind(xCards):
        print("4")
    elif is_two_pairs(xCards):
        print("3")
    elif is_one_pair(xCards):
        print("2")
    else:
        print("1")


if __name__ == "__main__":
    xCards = getCards()

    new = xCards.copy()
    for _ in xCards:
        x = new.pop()
        if x in new:
            print("Duplicate deal")
            exit()

processResult(xCards)
