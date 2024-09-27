A = 440
B = 1200
C = 130

x = int(input())
y = int(input())
z = int(input())

if x >= 0 and y >= 0 and z >= 0:
    total = A * x + B * y + C * z
    print(total)
