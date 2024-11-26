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

    sol = []
    cur = []
    weight = 0
    count = 0
    while se:
        i = se.pop(0)
        cur.append(i)
        weight += int(i[0])
        for j in se:
            if weight + int(j[0]) <= m:
                weight += int(j[0])
                cur.append(j)
                se.remove(j)

        if weight == m:
            count += 1
            sol.append(cur)
            cur = []
            weight = 0

    print(count)
    sol.sort(reverse=True)
    sol = [[j[1] for j in i] for i in sol]
    for i in sol:
        i.sort()
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    main()
