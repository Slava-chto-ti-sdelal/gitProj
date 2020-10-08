import sys
import argparse

def fib(n):
    n = int(n)
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', nargs='?')
    parser.add_argument('name', nargs='?')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    if len(sys.argv) == 2:
        print(fib(int(namespace.name)))
    else:
        print(fib(int(namespace.n)))