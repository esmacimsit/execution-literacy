def cpu_heavy(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total