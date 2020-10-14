def solution(a, b):
    for_adding = []
    for item in b:
        if item not in a:
            for_adding.append(item)
    return list(sorted(a + for_adding))
