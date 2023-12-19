def print_result(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        if isinstance(a, list):
            for i in a:
                print(i)
        elif isinstance(a, dict):
            for i, j in a.items():
                print(i, "=", j)
        else:
            print(a)
        return a
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


print('!!!!!!!!')
test_1()
test_2()
test_3()
test_4()