from functools import reduce

def flatten(lists):
    if len(lists) == 0:
        return lists
    if type(lists[0]) is type(list):
        return flatten(lists[0]) + flatten(lists[1:])
    return lists[:1] + flatten(lists[1:])


def reverse(lists):
    if len(lists) == 0:
        return lists

    elif len(lists) == 1:
        if isinstance(lists[0], list):
            return [reverse(lists[0])]
        else:
            return lists
    else:
        return reverse(lists[1:]) + reverse(lists[:1])


def compress(lists):
    if len(lists) <= 1:
        return lists
    elif lists[0] == lists[1]:
        return compress(lists[1:])
    else:
        return lists[:1] + compress(lists[1:])


def capitalized(items : list) -> list:
    return list(filter(lambda s: s[0].isupper(), items))

def longest(strings : list, from_start = True) -> object:
    return reduce(lambda one, two: one if len(one) > len(two) else one if (from_start) and len(one) == len(two) else two, strings)

def composition(f, g):
    return (lambda x: g(f(x)))

def n_composition(*functions):
    return reduce(composition, functions, lambda s: s)






