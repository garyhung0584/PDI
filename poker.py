def is_straight_flush(cards):
    return is_flush(cards) and is_straight(cards)


def is_four_of_a_kind(cards):
    num = [x[0] for x in cards]
    for i in num:
        if num.count(i) == 4:
            return True
    return False


def is_full_house(cards):
    if is_three_of_a_kind(cards) and is_one_pair(cards):
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
    for i in num:
        if num.count(i) == 3:
            return True
    return False


def is_two_pairs(cards):
    num = [x[0] for x in cards]
    pairs = 0
    for i in num:
        if num.count(i) == 2:
            pairs += 1
    return pairs == 2


def is_one_pair(cards):
    num = [x[0] for x in cards]
    for i in num:
        if num.count(i) == 2:
            return True
    return False


def getCards():
    NUMBERS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K")
    SUIT = ("C", "D", "H", "S")

    try:
        xCards = input().replace("10", "T").split()
        yCards = input().replace("10", "T").split()

        xCards = [
            (NUMBERS.index(x[0]) + 1, SUIT.index(x[1])) if len(x) == 2 else 0
            for x in xCards
        ]
        yCards = [
            (NUMBERS.index(x[0]) + 1, SUIT.index(x[1])) if len(x) == 2 else 0
            for x in yCards
        ]
        if 0 in xCards or 0 in yCards:
            raise Exception
    except:
        print("Error input")
        exit()

    return xCards, yCards


def processResult(xCards, yCards):
    if is_straight_flush(xCards) or is_straight_flush(yCards):
        return 9
    elif is_four_of_a_kind(xCards) or is_four_of_a_kind(yCards):
        return 8
    elif is_full_house(xCards) or is_full_house(yCards):
        return 7
    elif is_flush(xCards) or is_flush(yCards):
        return 6
    elif is_straight(xCards) or is_straight(yCards):
        return 5
    elif is_three_of_a_kind(xCards) or is_three_of_a_kind(yCards):
        return 4
    elif is_two_pairs(xCards) or is_two_pairs(yCards):
        return 3
    elif is_one_pair(xCards) or is_one_pair(yCards):
        return 2
    else:
        return 1


if __name__ == "__main__":
    xCards, yCards = getCards()

    for x in xCards:
        if x in yCards:
            print("Duplicate deal")
            exit()

    print(processResult(xCards, yCards))
