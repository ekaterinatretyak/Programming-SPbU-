import math

result = list(map(lambda x: math.factorial(x), filter(lambda x: math.factorial(x) % 3 == 0, range(50))))
print(result)