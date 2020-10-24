l = [121, 981, 540]
def solution(el):
    summary = 0
    while el > 0:
        summary = summary + (el % 10)
        el = el / 10
        continue
    return summary

result = [x for x in l if solution(x) <= 10]
print(result)