def sum_range(n, step):
    if n <= 0:
        return 0
    result = sum_range(n - step, step)
    return n + result


def factorial(n):
    if n == 0:
        return 1
    n_minus_1 = factorial(n - 1)
    return n * n_minus_1


if __name__ == '__main__':
    print(factorial(5))
    # print(sum_range(5, 1))
    # print(sum_range(5, 9))
    # print(sum_range(8, 2))
