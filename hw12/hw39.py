def max_gold(n, start, caves):
    def dfs(cave, visited):
        if cave == 0 or cave in visited:
            return 0

        visited.add(cave)
        g, y, z = caves[cave]

        gold_y = dfs(y, visited.copy())
        gold_z = dfs(z, visited.copy())

        return g + max(gold_y, gold_z)

    return dfs(start, set())


# Input reading
def main():
    n, start = map(int, input().split())
    caves = {}

    for _ in range(n):
        data = list(map(int, input().split()))
        cid, g, y, z = data
        caves[cid] = (g, y, z)

    result = max_gold(n, start, caves)
    print(result)


if __name__ == "__main__":
    main()
