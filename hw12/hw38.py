from collections import deque, defaultdict


def find_shortest_path_with_rest_stop(n, x, z, rest_stops, connections):
    # 建立部落圖
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    # BFS 搜尋最短路徑
    def bfs(start, end):
        queue = deque([(start, [start])])  # (當前部落, 路徑)
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current == end:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None

    # 搜尋從 X 經過某個休息點到 Z 的最短路徑
    shortest_path = None
    best_rest_stop = None

    for rest_stop in rest_stops:
        path_to_rest = bfs(x, rest_stop)
        path_from_rest = bfs(rest_stop, z)

        if path_to_rest and path_from_rest:
            total_path = path_to_rest[:-1] + path_from_rest
            if not shortest_path or len(total_path) < len(shortest_path):
                shortest_path = total_path
                best_rest_stop = rest_stop

    # 輸出結果
    if not shortest_path:
        return "NO"
    else:
        return f"{best_rest_stop}\n{' '.join(map(str, shortest_path))}"


# 讀取輸入
def main():
    n, x, z = map(int, input().split())
    rest_stops = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(n)]

    # 計算並輸出結果
    result = find_shortest_path_with_rest_stop(n, x, z, rest_stops, connections)
    print(result)


if __name__ == "__main__":
    main()
