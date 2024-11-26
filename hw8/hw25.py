def main():
    temp = []
    n = int(input())
    d = int(input())
    for i in range(n):
        st = input()
        temp.append(st)

    for i in range(n):
        depth = [0] * 3
        length = len(temp[i])
        cur = temp[i]
        record = ""
        lock = 0
        for j in range(length):
            if cur[j] == "{":
                depth[0] += 1
                lock = 1
            if cur[j] == "}":
                if lock != 1:
                    print("fail7")
                    break
                depth[0] -= 1
            if cur[j] == "[":
                depth[1] += 1
                lock = 2
            if cur[j] == "]":
                if lock != 2:
                    print("fail")
                    break
                depth[1] -= 1
            if cur[j] == "(":
                depth[2] += 1
                lock = 3
            if cur[j] == ")":
                if lock != 3:
                    print("fail")
                    break
                depth[2] -= 1

            if sum(depth) == d:
                record += cur[j]

        if sum(depth) == 0:
            print("PASS")


if __name__ == "__main__":
    main()
