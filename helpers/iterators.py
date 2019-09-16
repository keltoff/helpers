

def pairs(values):
    iterator = values.__iter__()
    last = iterator.next()
    for i in iterator:
        yield last, i
        last = i


def flatten(*args):

    if len(args) > 1:
        return flatten(tuple(args))

    items = []
    for t in args[0]:
        if issubclass(t.__class__, tuple):
            items.extend(flatten(t))
        else:
            items.append(t)
    return tuple(items)


def all_combinations(*iterables):
    params = list(iterables)
    outer_param = params.pop()

    for val in outer_param:
        if len(params) > 0:
            for rest in all_combinations(*params):
                yield flatten(val, rest)
        else:
            yield val


if __name__ == '__main__':
    for a, b in pairs(range(10)):
        print('{}-{}'.format(a, b))

    print('\n')

    print(flatten((((1)), 2, 3, (4, (5), 6))))

    print('\n')

    for x in all_combinations(range(3), range(3), ['x', 'y']):
        # print('{} {} {}'.format(a, b, c))
        print(x)
