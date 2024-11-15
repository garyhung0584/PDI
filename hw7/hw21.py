def compute(n, m, a, b, c, d):
    days = [0 for _ in range(m + 1)]
    days[0] = a
    start = 0

    for i in range(m):
        if i >= c:
            d = d + days[start] / n
            if d > 1:
                d = 1
            start += 1

        days[i + 1] = int(
            min(
                sum(days[start : i + 1]) * (b / c) * (1 - d),
                max(n * (1 - d) - sum(days[start : i + 1]), 0),
            )
        )

        print(f"{i+1} {sum(days[start:i+1]):d} {days[i]} {days[start-1]}")
    print(sum(days[:m]))


def main():
    n = int(input())
    m = int(input())
    a = int(input())
    b = float(input())
    c = int(input())
    d = float(input())

    compute(n, m, a, b, c, d)


if __name__ == "__main__":
    main()
