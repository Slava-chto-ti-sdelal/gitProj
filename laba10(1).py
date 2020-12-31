import pickle


def pickle_test(inp):
    with open('temp.pickle', 'wb') as f:
        pickle.dump(inp, f)

    with open('temp.pickle', 'rb') as f:
        out = pickle.load(f)

    assert type(inp) == type(out)

    if hasattr(inp, '__iter__'):
        assert [i for i in inp] == [j for j in out], 'no'
    else:
        assert inp == out, 'no'

    print('ok')
    return None


data = iter([1, 2, 3, 4, 5])
pickle_test(data)