def nMark(n, mark="*"):
    for j in range(n):
        print(mark, end="")


def myPrint(N):
    for i in range(N):
        nMark(N - i - 1, ".")
        nMark(2 * i + 1)
        nMark(N - i - 1, ".")
        print()


myPrint(6)
