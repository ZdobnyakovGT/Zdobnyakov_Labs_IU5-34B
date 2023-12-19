# Пример:

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def field(items, *args):
    assert len(args) > 0
    for i in items:
        result = {}
        for key in args:
            if key in i and i[key] is not None:
                result[key] = i[key]

        if len(result) == 1:
            yield list(result.values())[0]
        elif len(result) > 1:
            yield result


print(list(field(goods, 'title')))