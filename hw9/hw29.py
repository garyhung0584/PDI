def generate_permutations(s):
    if len(s) == 1:
        return [s]

    perms = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i + 1 :]
        for p in generate_permutations(remaining):
            perms.append(char + p)
    return perms


def generate_combinations(s, n):
    def combine(current, remaining, length):
        if len(current) == length:
            combinations.append(current)
            return

        for i in range(len(remaining)):
            combine(current + remaining[i], remaining[i + 1 :], length)

    combinations = []
    combine("", s, n)
    return combinations


def main():
    # 輸入與驗證
    M = input()

    N = int(input())

    # 所有排列
    all_permutations = generate_permutations(M)
    print(", ".join(all_permutations))

    # 只取 N 個字元的結合
    n_combinations = generate_combinations(M, N)
    print(", ".join(n_combinations))


if __name__ == "__main__":
    main()
