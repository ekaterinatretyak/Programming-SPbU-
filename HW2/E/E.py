def solution(a, b):
    a += 1
    b -= 1
    if b > 0:
        return solution(a, b)
    else:
        return a
