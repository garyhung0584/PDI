def ic(ins):
    for i in ins:
        i = [int(i[j]) for j in range(len(i))]
        ans = r(i)

        print(
            f"{ans//8}{(ans-(ans//8)*8)//4}{((ans-(ans//8)*8)-((ans-(ans//8)*8)//4)*4)//2}{(((ans-(ans//8)*8)-(ans//4)*4)-(((ans-(ans//8)*8)-(ans//4)*4)//2)*2)//1}"
        )


def r(i):
    if 1 in i[: len(i) - 1]:
        if i[len(i) - 1] == 0:
            return r(i[: len(i) - 1]) + 1
        else:
            for j in range(len(i) - 1, -1, -1):
                if i[j] == 0:
                    i[j] = 1
                    break
                else:
                    i[j] = 0
            if not (1 in i):
                i[0] = 1
                return r(i[: len(i)]) + 1
            return r(i[: len(i) - 1]) + 1
    else:
        return 0


def main():
    ins = []
    while True:
        m = input()
        if m == "-1":
            break
        ins.append(m)
    ic(ins)


if __name__ == "__main__":
    main()
