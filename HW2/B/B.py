# def solution(x):
#
#     a = x[:x.find('h') + 1]
#     b = x[x.find('h') + 1:x.rfind('h')]
#     c = x[x.rfind('h'):]
#     x = a + b.replace('h', 'H') + c
#
#     newstr = x[0] + ''.join([x[i] for i in range(1, len(x)) if i % 3 != 0])
#     for a in range(len(x)):
#         if x[a] == '1':
#             newstr = newstr.replace('1', 'one')
#
#     return newstr
# print(solution('ktwcqzqdkqc3tdtiwkqiowttr03bqdfqcc19olkw9r5rii1obbcoclrqo5qqw5d013obicowih3l3c9l1orczv1bfvd5wfikl5zwtlz1f5ow01loofd1d0qz9vt3l3tft5i0orrltokt'))

def solution(x):
    a = x[:x.find('h') + 1]
    b = x[x.find('h') + 1:x.rfind('h')]
    c = x[x.rfind('h'):]
    x = a + b.replace('h', 'H') + c

    x = x[0] + ''.join([x[i] for i in range(1, len(x)) if i % 3 != 0])

    for a in range(len(x)):
        if x[a] == '1':
            x = x.replace('1', 'one')
    return x
print(solution('bl9iki9ttbcrwzko0q1qqlwrqdrfdwidr9fd5wtrqr3oc905fqb0zkdlih0vikhfb3kfrrfqhb3bfld3w0zrr901if0bvitzl00l5h5tokvvd03dwz0wql9lqfcltciwf91k9cicwihd5to35vt0qzw3drwhclvo3izllhwv10rlohtkitt1dbhvob3wo9bq0ikk50dwb1o5rfkorw5w1rdzh1flqohrrtbwztoritd3qo03lckd5clvkqo5flzkq3fktlr15dothtkbilzv1lhzrkkvdzbrivihow0loz3wokdrk9kz1kv15ldhww3191ico9qf0tli3kkwvc5rqht930wh55o9fi19w51ihko5rdf5orql3rzobilq5lbhl5vqfvhr0bk90zz0wiwilttzf33lwrtvhz09qlqb3l3ocwtdrb3o950z195ki5kvdwc1ri09d1ho1oh5vl1bfb5dzv5v0d0rvblhbvo9vzbtr511dhqb0ih10bcwzc153kk5ddc0d99fwtoocr00klcf3kq11w1wdz00hll93bthh9qvldtlblrclqlki0vcvwtlwirt9btz0k50twktz01r3dw31wlbfk5iw9q19k3rwv1fb0wofc0vi3lcdvd5qhobvcodvfobblwllzz9h1o0rwltz1zoqv5cvdfhtb93qzqdf'))