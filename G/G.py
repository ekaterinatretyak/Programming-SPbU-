def solution(a, b):
    for_adding = []
    result = []
    for item in b:
        if item not in a:
            for_adding.append(item)
    for_adding = a + for_adding
    while for_adding:
        result.append(for_adding.pop(for_adding.index(min(for_adding))))
    return result