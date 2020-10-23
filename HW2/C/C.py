def solution(arr):
    res = []
    while arr:
        res.extend(list(arr.pop(0)))
        arr = list(zip(*arr))
        arr.reverse()
    return res
