import time
from cpu_workload import cpu_heavy

TASKS = 4
N = 30_000_000

start = time.perf_counter()

for _ in range(TASKS):
    cpu_heavy(N)

end = time.perf_counter()
print(f"SYNC total time: {end - start:.2f}s")

# SYNC total time: 3.57s