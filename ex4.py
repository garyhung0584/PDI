def nMark(n, mark="#"):
    for i in range(n):
        print(mark, end="")


def tower(n):
    for i in range(n, -n, -2):
        if i < 0:
            i -= 2
        print(f"{abs(i)}", end="")


def myPrint(N):
    for i in range(N):
        nMark(N - i - 1, "#")
        tower(2 * i + 1)
        print()


myPrint(5)
