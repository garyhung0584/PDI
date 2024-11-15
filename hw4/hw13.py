n = int(input())
if n <= 0:
    print("Error")


def myPrint(i):
    i = (2 * i) - 1
    for j in range(i, -i + 1, -2):
        if j <= 0:
            j -= 2
        print(i - abs(j) + 1, end="")


for i in range(n - 1, -n, -1):
    print("*" * (abs(i)), end="")
    myPrint(n - abs(i))
    print()
