def solution(arr):
    count = 1
    max = 1
    for i in range(len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            if count > max:
                max = count
                count = 1
            else:
                count = 1
    return max