import random


def gen_random(num_count, begin, end):
    for i in range(num_count):
        print(random.randint(begin, end))


gen_random(5, 1, 3)