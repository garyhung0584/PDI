def main():
    while 1:
        n = input()
        if n == "-1":
            break
        lst = []
        for i in n.split():
            lst.append(int(i, 16))
        lst.sort()
        mid = 0
        if len(lst) % 2 == 0:
            mid = (lst[int(len(lst) / 2 - 1)] + lst[int(len(lst) / 2)]) / 2
        else:
            mid = lst[int((len(lst) - 1) / 2)]
        print(lst[0] + lst[-1] + mid)


main()
