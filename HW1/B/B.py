def solution(n):
    if n == 0:
        return ""
    else:
        part1 = "   _~_   "
        part2 = "  (o o)  "
        part3 = " /  V  \ "
        part4 = "/(  _  )\\"
        part5 = "  ^^ ^^  "
        result = part1 * n + '\n' + part2 * n + '\n' + part3 * n + '\n' + part4 * n + '\n' + part5 * n
        return result