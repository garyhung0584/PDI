nums = input().split()
nums = [int(x) for x in nums]

print([nums[i] + nums[i + 1] for i in range(len(nums) - 1)])
