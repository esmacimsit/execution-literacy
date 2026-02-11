import time
import threading
from cpu_workload import cpu_heavy

TASKS = 4
N = 30_000_000

threads = []
start = time.perf_counter()

for _ in range(TASKS):
    t = threading.Thread(target=cpu_heavy, args=(N,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()
print(f"THREAD total time: {end - start:.2f}s")

# THREAD total time: 3.30s