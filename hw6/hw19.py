n = int(input())
map = []
for i in range(n):
    row = input().split(" ")
    row = [int(j) for j in row]
    map.append(row)

def search(pos):
    if map[pos//n][pos%n] == 1:
        return 0
    else:
        temp = 0
        for i in range(9):
            if (pos//n)+(i//3)-1 < 0 or (pos%n)+(i%3)-1 < 0:
                continue
            try:
                temp += map[(pos//n)+(i//3)-1][(pos%n)+(i%3)-1]
            except:
                pass
    return temp

result = [[search(i*n+j) for j in range(n)] for i in range(n)]

for i in result:
    for j in i:
        print(j,end=" ")
    print()