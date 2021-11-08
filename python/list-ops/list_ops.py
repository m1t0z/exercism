def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    concated = []
    for list in lists:
        for item in list:
            concated.append(item)
    return concated


def filter(function, list):
    filtered = []
    for item in list:
        if function(item):
            filtered.append(item)
    return filtered


def length(list):
    cnt = 0
    for _ in list:
        cnt += 1
    return cnt


def map(function, list):
    mapped = []
    for item in list:
        mapped.append(function(item))
    return mapped


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for item in list[::-1]:
        accumulator = function(item, accumulator)
    return accumulator


def reverse(list):
    reversed = []
    for item in list[::-1]:
        reversed.append(item)
    return reversed
