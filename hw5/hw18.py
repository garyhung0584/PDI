nums = input().split()
target = int(input())
ans = []
nums = [int(i) for i in nums]

for i in range(len(nums)):
    j = i+1
    while j < len(nums):
        if (nums[i]+ nums[j]) == target:
            ans.append([i,j])
        j += 1

val = [ i[0] * i[1] for i in ans]
print(sorted(ans[val.index(max(val))], reverse=True))


    