def _flatten(iterable):
    for item in iterable:
        if type(item) is list:
            yield from _flatten(item)
        elif item is not None:
            yield item


def flatten(iterable):
    return list(_flatten(iterable))
