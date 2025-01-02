import re


def main():
    PRIME = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

    front = input()
    backs = input().split(" ")
    piece = input()

    back = "|".join(backs)
    exp = front + "[A-Z]+?(?:" + back + ")"

    x = re.findall(exp, piece)

    x = [i[4:-3] for i in x if len(i[4:-3]) in PRIME]
    x.sort(key=lambda x: (len(x), x))

    if not x:
        print("No gene")
        return

    for i in x:
        print(i)


if __name__ == "__main__":
    main()
