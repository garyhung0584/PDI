import math

a = int(input())
b = int(input())
c = int(input())


discri = b**2 - 4 * a * c
if discri < 0:
    absDiscri = math.sqrt(abs(discri)) / (2 * a)
    if absDiscri == 0:
        print(f"{-b / (2 * a):.1f}+{abs(math.sqrt(abs(discri)) / (2 * a)):.1f}i")
    else:
        print(f"{-b / (2 * a):.1f}+{abs(math.sqrt(abs(discri)) / (2 * a)):.1f}i")
        print(f"{-b / (2 * a):.1f}-{abs(math.sqrt(abs(discri)) / (2 * a)):.1f}i")
elif discri == 0:
    print(f"{-b / (2 * a):.1f}")
else:
    x1 = (-b + math.sqrt(discri)) / (2 * a)
    x2 = (-b - math.sqrt(discri)) / (2 * a)
    if x1 != x2:
        print(f"{x1:.1f}\n{x2:.1f}")
