def find_max_gold(n, start_cave, caves):
    def dfs(cave_id, visited):
        if cave_id == 0 or cave_id in visited:
            return 0

        visited.add(cave_id)
        gold, next_y, next_z = caves[cave_id]

        # 嘗試選擇 Y 或 Z 路徑
        gold_y = dfs(next_y, visited.copy())
        gold_z = dfs(next_z, visited.copy())

        return gold + max(gold_y, gold_z)

    return dfs(start_cave, set())


# 讀取輸入
def main():
    n, start_cave = map(int, input().split())
    caves = {}

    for _ in range(n):
        data = list(map(int, input().split()))
        cave_id, gold, next_y, next_z = data
        caves[cave_id] = (gold, next_y, next_z)

    # 計算最大黃金數量
    max_gold = find_max_gold(n, start_cave, caves)
    print(max_gold)


if __name__ == "__main__":
    main()
