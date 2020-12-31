class Terminate(Exception):
    pass


class Connect(Exception):
    pass


def connect_user(username):
    with open('message.txt', 'w', encoding='utf-8') as f:
        yield from write_to_file(f)


def write_to_file(f_obj):
    while True:
        try:
            a = yield
            f_obj.writelines(a)
            f_obj.writelines('\n')
        except Terminate:
            print('finish')
            break
    f_obj.close()


def plan():
    user = []
    while True:
        try:
            username = yield
            user.append(username)
        except Connect:
            yield from connect_user()


coroutine = plan()
next(coroutine)
coroutine.throw(Connect)
coroutine.send('hello')
coroutine.send('Hi!')
coroutine.throw(Terminate)
coroutine.close()
