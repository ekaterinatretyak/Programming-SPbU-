l = [1, 3, 5, 7, 45]
result = [x for ind, x in enumerate(l) if ind % 2 != 0]
print(result)