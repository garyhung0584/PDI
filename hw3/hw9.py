n = int(input())

if n < 2 or n > 20:
    exit()


def square(n):
    print("*" * n)
    for _ in range(n - 2):
        print("*" + "#" * (n - 2) + "*")
    print("*" * n)


def triangle(n):
    for i in range(n):
        print("#" * (n - i - 1) + "*" * (1 + 2 * i))


if n % 2 == 0:
    square(n)
else:
    triangle(n)
