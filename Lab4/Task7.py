import json
import time


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.end_time = time.time() - self.start_time
        print('time:', self.end_time)


def field(items, *args):
    # assert len(args) > 0
    for i in items:
        result = {}
        for key in args:
            if key in i and i[key] is not None:
                result[key] = i[key]

        if len(result) == 1:
            yield list(result.values())[0]
        elif len(result) > 1:
            yield result


import random


def gen_random(num_count, begin, end):
    rand = []
    for i in range(num_count):
        rand.append(random.randint(begin, end))
    return rand


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


class Unique(object):
    def __init__(self, items, **kwargs):
        if isinstance(items, (list, tuple)):
            self.items = iter(items)
        else:
            self.items = items
        self.ignore_case = kwargs.get('ignore_case', False)
        self.garb = []

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.items)
            except StopIteration:
                raise  StopIteration
            if self.ignore_case and isinstance(item, str):
                word = item.lower()
            else:
                word = item
            if word not in self.garb:
                self.garb.append(word)
                return item



















path = "job.json"


@print_result
def f1(arg):

    print(list(Unique(field(arg, "job-name"))))
    return list(Unique(field(arg, "job-name")))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith("Программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda s: f"{s} с опытом Python", arg))


@print_result
def f4(arg):
    sp = []
    salaries = gen_random(len(arg), 100000, 200000)
    for profession, salary in zip(arg, salaries):
        sp.append([profession, "salary", salary, 'rub'])
    return sp


# with open(path) as f:
#     dat = json.load(f)

import io

with io.open(path, encoding='utf-8') as f:
    dat = json.load(f)

with cm_timer_1():
    f4(f3(f2(f1(dat))))
