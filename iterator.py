class reverse_iter:
    def __init__(self, l):
        self.l = l
        self.i = len(l)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i != 0:
            self.i -= 1
            self.cur = self.l[self.i]
            return self.cur
        else:
            raise StopIteration()

it = reverse_iter([5, 11, 5, 7,  3, 9])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))