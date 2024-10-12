def mySum(m, n, step):
    return sum(range(m, n + 1, step))


def main():
    m = int(input("Input a min number:"))
    n = int(input("Input a max number:"))
    step = int(input("Input a step number:"))
    main_sum = mySum(m, n, step)
    print("sum (%d ~ %d) = %d" % (m, n, main_sum))


main()
