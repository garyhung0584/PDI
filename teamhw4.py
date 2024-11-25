def f(data, prefix=""):
    n = len(data)
    if n == 0:
        print(prefix)
    else:
        for i in range(n):
            x = data[i]
            y = data[:i] + data[i + 1 :]
            f(y, prefix + x)


f("abcd")
