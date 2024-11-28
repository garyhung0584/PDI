def getRes(st, d):
    n = len(st)
    layer = []
    ans = ""
    for i in range(n):
        if st[i] == "[" or st[i] == "{" or st[i] == "(":
            layer.append(st[i])
        elif st[i] == "]" or st[i] == "}" or st[i] == ")":
            if not layer:
                return "fail"
            if st[i] == "]" and layer[-1] == "[":
                layer.pop()
            elif st[i] == "}" and layer[-1] == "{":
                layer.pop()
            elif st[i] == ")" and layer[-1] == "(":
                layer.pop()
            else:
                return "fail"
        elif len(layer) == d:
            ans += st[i]

    if layer:
        return "fail"
    else:
        ans = ans if ans else "EMPTY"
        return "pass," + ans


def main():
    temp = []
    n = int(input())
    d = int(input())
    for _ in range(n):
        st = input()
        temp.append(st)

    res = []
    for i in temp:
        res.append(getRes(i, d))

    for i in res:
        print(i)


if __name__ == "__main__":
    main()
