# primenumber factorization by fermats theorem.
import math


def main():
    n = 1836 # The number which will be factorized.
    step = 0
    while True:
        step += 1
        x = get_x(n, step)
        if (x ** 2 - n) ** 0.5 - int((x ** 2 - n) ** 0.5) == 0:
            a = x + (x ** 2 - n) ** 0.5
            b = x - (x ** 2 - n) ** 0.5
            print('x: ', int(x))
            print('a:', int(a))
            print('b:', int(b))
            break

def get_x(n, step):
    return abs(int(n ** 0.5)) + step


def checkSquare(x):
    # Find floating point value of
    # square root of x.
    sqr = math.sqrt(x)
    # If square root is an integer
    return ((sqr - math.floor(sqr)) == 0)


if __name__ == '__main__':
    main()
