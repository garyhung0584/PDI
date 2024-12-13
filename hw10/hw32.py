def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1


def is_narcissistic_number(num):
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return sum(d**power for d in digits) == num


def digit_sum_to_single(num):
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    n = int(input())

    happy = is_happy_number(n)
    narcissistic = is_narcissistic_number(n)

    digit_sum = digit_sum_to_single(n)

    if happy and narcissistic:
        print(f"{n} is both a happy number and a narcissistic number.")
        print(f"F({digit_sum}) = {fibonacci(digit_sum)}")
    elif happy:
        print(f"{n} is a happy number.")
        print(f"F({digit_sum}) = {fibonacci(digit_sum)}")
    elif narcissistic:
        print(f"{n} is a narcissistic number.")
        print(f"{digit_sum}! = {factorial(digit_sum)}")
    else:
        print(f"{n} is neither a happy number nor a narcissistic number.")
        print(f"{digit_sum}! = {factorial(digit_sum)}")


if __name__ == "__main__":
    main()
