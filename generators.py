def integers():
    n = 1
    while True:
        yield n
        n += 1

def squares():
    for item in integers():
        yield item * item

def take(x, gener):
    res = []
    for el in range(x):
        res.append(next(gener))
    return res

    # or:
    # res = list(next(gener) for el in range(x))
    # return res

print(take(5, squares()))
