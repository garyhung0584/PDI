import math

a = int(input())
b = int(input())
c = int(input())

x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
if x1 != x2:
    print(f"{x1:.1f}\n{x2:.1f}")
else:
    print(f"{x1:.1f}")
