def game(p1, p2, computer, draw1, draw2, draw3):
    p1 = clean(p1)
    p2 = clean(p2)
    computer = clean(computer)

    # Player 1 draws from Player 2
    if draw1 in p2:
        p1.append(draw1)
        p2.remove(draw1)
        p1 = clean(p1)
    else:
        print("Error")
        return

    # Player 2 draws from Computer
    if draw2 in computer:
        p2.append(draw2)
        computer.remove(draw2)
        p2 = clean(p2)
    else:
        print("Error")
        return

    # Computer draws from Player 1
    if draw3 in p1:
        computer.append(draw3)
        p1.remove(draw3)
        computer = clean(computer)
    else:
        print("Error")
        return

    # Print hands after all draws
    print(" ".join(p1))
    print(" ".join(p2))
    print(" ".join(computer))


def clean(hand):
    """Remove pairs from a hand based on card numbers."""
    numbers = [card[1:] for card in hand]
    pairs = {num for num in numbers if numbers.count(num) == 2}

    # Remove all cards with paired numbers
    return [card for card in hand if card[1:] not in pairs]


def main():
    p1 = input().split(" ")
    p2 = input().split(" ")
    computer = input().split(" ")
    draw1 = input()
    draw2 = input()
    draw3 = input()

    game(p1, p2, computer, draw1, draw2, draw3)


if __name__ == "__main__":
    main()
