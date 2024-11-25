def main():
    field = []
    for _ in range(4):
        row = input().split()
        field.append(row)

    res = field
    ANS = ["1", "2", "3", "4"]
    game = True
    while game:
        for i in range(4):
            for j in range(4):
                if field[i][j] == "0":
                    res[i][j] = ANS
                    for k in range(4):
                        if field[i][k] in res[i][j]:
                            res[i][j].remove(field[i][k])
                    for k in range(4):
                        if field[k][j] in res[i][j]:
                            res[i][j].remove(field[k][j])
                    for k in range(4):
                        if field[i // 2 * 2 + k // 2][j // 2 * 2 + k % 2] in res[i][j]:
                            res[i][j].remove(
                                field[i // 2 * 2 + k // 2][j // 2 * 2 + k % 2]
                            )

                    if len(res[i][j]) == 1:
                        field[i][j] = res[i][j][0]

        game = False
        for i in range(4):
            for j in range(4):
                if "0" in res[i][j]:
                    game = True

    for i in res:
        for j in i:
            print(j, end=" ")


if __name__ == "__main__":
    main()
