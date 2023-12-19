import random

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']


def gen_random(num_count, begin, end):
    rand = []
    for i in range(num_count):
        rand.append(random.randint(begin, end))
    for i in rand:
        print(i)

    return rand


class Unique(object):
    def init(self, items, **kwargs):
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
                raise StopIteration
            if self.ignore_case and isinstance(item, str):
                word = item.lower()
            else:
                word = item
            if word not in self.garb:
                self.garb.append(word)
                return item



a = Unique(data2)
it = iter(a)
for i in it:
    print(i)


a = Unique(data1)
it = iter(a)
for i in it:
    print(i)
