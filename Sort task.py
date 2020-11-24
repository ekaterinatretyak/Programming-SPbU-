def sorting(mystring):
    res = "".join(mystring[0])
    for char in mystring:
        for sorted_key in res:
            if ord(char) < ord(sorted_key):
                res = res[:res.index(sorted_key)] + char + res[res.index(sorted_key):]
                break
        if ord(char) > ord(sorted_key):
                res = res + char
    print("Исходная строка: ", mystring)
    print("Отсортированная строка: ", res)
    print(type(res))

sorting("62tgrews5GttoaAkr")