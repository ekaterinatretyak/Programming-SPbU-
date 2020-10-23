def solution(n, k):
    alive = [x for x in range(1, n + 1)]
    while len(alive) > 1:
        victim = (k - 1) % len(alive)
        alive.pop(victim)
        alive = alive[victim:] + alive[:victim]
    return ' '.join(str(res) for res in alive)

