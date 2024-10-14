nums = set(map(int, input().split()))


def f(data: list):
    data.remove(max(data))
    print(max(data))


f(nums)
