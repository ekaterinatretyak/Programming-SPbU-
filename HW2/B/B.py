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