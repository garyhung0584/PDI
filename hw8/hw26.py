def processDeliver(se, m):
    """
    處理貨物配送並輸出結果。
    :param se: 貨物編號列表
    :param m: 貨車載重限制
    """
    solution = []
    current = []
    while se:
        current.append(se[0])
        for i in se[1:]:
            if int(i[0]) + sum([int(j[0]) for j in current]) <= m:
                current.append(i)
        if sum([int(j[0]) for j in current]) == m:
            solution.append(current)
            for j in current:
                se.remove(j)
            current = []

    return [[j[1] for j in i] for i in sorted(solution)]


def main():
    se = input().split(" ")
    m = int(input())
    if m < 1 or m > 10:
        print("Input Error")
        return
    total = 0
    for i in se:
        if se.count(i) > 1:
            print("Duplicated ID")
            return
    for i in se:
        if int(i[0]) > m:
            print("Load limit exceeded")
            return
        total += int(i[0])
    if total % m != 0:
        print("Cannot be delivered")
        return

    solution = processDeliver(se, m)
    solution = sorted([sorted(i) for i in solution])
    print(len(solution))
    solution.sort(key=lambda x: (len(x), x))
    for i in solution:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    main()
