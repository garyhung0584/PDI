from collections import Counter


def median(lst):
    s = sorted(lst)
    return (s[len(s) // 2] + s[~(len(s) // 2)]) / 2


def mode(lst):
    c = Counter(lst)
    m = max(c.values(), default=None)
    return (
        []
        if m and list(c.values()).count(m) == len(c)
        else [k for k, v in c.items() if v == m]
    )


while True:
    input_str = input("Enter numbers separated by spaces (or 'exit' to quit): ")
    lst = list(map(int, input_str.split()))
    print("Median:", median(lst))
    print("Mode:", mode(lst))
