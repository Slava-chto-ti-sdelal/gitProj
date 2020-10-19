def cool_wrap(func):
    def wrapper(inlist):
        original = func(inlist)
        if not original:
            return('Нет')
        elif original > 10:
            return('Очень много')
        else:
            return original
    return wrapper


@cool_wrap
def f(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count