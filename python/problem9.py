import euler


ANSWER = 31875000
SUM = 1000


def main():
    for a in range(int((SUM // 2) ** 0.5)):
        for trio in euler.pythagorean_trio(a):
            if sum(trio) == SUM:
                return trio[0] * trio[1] * trio[2]
    return 0


if __name__ == '__main__':
    print(main())