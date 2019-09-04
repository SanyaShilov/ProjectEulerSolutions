import euler


ANSWER = 18613426663617118
LIMIT = 1000000


def chinese_remainder(divisors, remainders):
    result = 0
    product = euler.product(divisors)
    for divisor, remainder in zip(divisors, remainders):
        product_i = product // divisor
        result += remainder * mul_inv(product_i, divisor) * product_i
    return result % product


def mul_inv(a, b):
    r1, r2 = a, b
    prev, tmp = 1, 0
    # r1 = prev * a + not_calculated * b; r2 = tmp * a + not_calculated * b
    while r1 > 1:
        r1, r2, q = r2, r1 % r2, r1 // r2
        prev, tmp = tmp, prev - q * tmp
    if prev < 0:
        prev += r2
    return prev


def main():
    prime_list = euler.prime_list(LIMIT + 1000)
    total = 0
    ten = 1
    for i in range(2, len(prime_list)):
        pr1 = prime_list[i]
        if pr1 > LIMIT:
            break
        if ten < pr1:
            ten *= 10
        pr2 = prime_list[i + 1]
        n = chinese_remainder((ten, pr2), (pr1, 0))
        total += n
    return total


if __name__ == '__main__':
    print(main())
