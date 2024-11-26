def main():
    field = []
    for _ in range(4):
        row = input().split()
        field.append(row)

    ANS = ["1", "2", "3", "4"]
    res = [[j if j != "0" else ANS for j in i] for i in field]
    game = True
    while game:
        for i in range(4):
            for j in range(4):
                if isinstance(res[i][j], list):
                    for k in res[i][j]:
                        if k in res[i]:
                            res[i][j].remove(k)
                            continue
                        if k in [res[m][j] for m in range(4)]:
                            res[i][j].remove(k)
                    if len(res[i][j]) == 1:
                        field[i][j] = res[i][j][0]
                        res[i][j] = res[i][j][0]

        game = False
        for i in range(4):
            for j in range(4):
                if "0" in field[i][j]:
                    print(field[i][j], i, j)
                    game = True
                    break

    # for i in field:
    #     for j in i:
    #         print(j, end=" ")


if __name__ == "__main__":
    main()
