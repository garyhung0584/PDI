def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


nums = input().split()
nums = [int(x) for x in nums]
nums.sort()

output = [x for x in nums if is_prime(x)]
print(output if output else "No prime number ")
