import itertools

def print_map(function, iterable): #цикл for
    i = iter(iterable)
    while i < iterable:
        print(function(next(i)))


#Фибонначи
def fib(n):
    n = int(n)
    f1 =0
    f2 =1
    for i in range(n):
        a = f1
        f1 = f2
        f2 = f1 + a
        yield f1


n = input()

for f in fib(n):
    print(f, end =' ')
print()

#номерные упр
def get_cartesian_product(a, b):
    return list(itertools.product(a, b))

a = [1,2]
b = [3,4]
print(get_cartesian_product(a, b))

def get_permutations(s, n):
    return sorted([''.join(x) for x in itertools.permutations(s, n)])

print(get_permutations('cat',2))


def get_combinations(s, n):
    a = sorted([''.join(sorted(x)) for i in range(1, n+1) for x in itertools.combinations(s, i)])
    a.sort(key=lambda x: len(x))
    return a

print(get_combinations("cat", 2))


def get_combinations_with_r(s, n):
    return sorted([''.join(sorted(x)) for x in itertools.combinations_with_replacement(s, n)])

print(get_combinations_with_r("cat", 2))

def compress_string(s):
    A = []
    B = []
    for k, g in itertools.groupby(s):
        A.append(len(list(g)))
        B.append(int(k))
    return list(zip(A, B))

print(compress_string('1222311'))


def maximize(lists, m):
    A = [max(lst) ** 2 for lst in lists]
    B = [p for p in itertools.accumulate(A)]
    return max([x % m for x in B])


lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]

print(maximize(lists, m=1000))

