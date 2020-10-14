def solution(total):
    hours = total % (60 * 24) // 60
    minutes = total % 60
    return str(hours) + ' ' + str(minutes)