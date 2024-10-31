def myPrint(n, m):
    if m < -1 or m > 2:
        print("ERROR")
        return

    for i in range(n):
        for j in range(n):
            if m == 0:
                print(f"{n * i + j:-3d}", end="")
            elif m == 1:
                print(f"{n * (n - i - 1) + j:-3d}", end="")
            else:
                print(f"{n * (n - j - 1) + i:-3d}", end="")

        print()


if __name__ == "__main__":
    n = int(input())
    if n < 1 or n > 10:
        print("ERROR")
        exit()
    m = int(input())
    mlist = []
    while m != -1:
        mlist.append(m)
        m = int(input())

    for i in mlist:
        myPrint(n, i)
