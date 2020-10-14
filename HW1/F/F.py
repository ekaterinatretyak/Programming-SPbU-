def solution(n):
    answer = []
    for digit in range(100):
        if digit == 0:
            st = 1
        else:
            st = st * 2
        if st <= n:
            answer.append(st)
    return answer