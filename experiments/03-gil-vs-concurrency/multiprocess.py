from multiprocessing import Process
import time
from cpu_workload import cpu_heavy

TASKS = 4
N = 30_000_000


def main():
    processes = []
    start = time.perf_counter()

    for _ in range(TASKS):
        p = Process(target=cpu_heavy, args=(N,)) # separate process with its own memory space
        p.start()
        processes.append(p)

    for p in processes:
        p.join() # wait for all processes to finish

    end = time.perf_counter()
    print(f"PROCESS total time: {end - start:.2f}s")


if __name__ == "__main__":
    main() # main guard is required for multiprocessing on Windows or MacOS

# PROCESS total time: 1s