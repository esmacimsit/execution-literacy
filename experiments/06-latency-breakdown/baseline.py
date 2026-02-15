import time
from workload import full_workload

if __name__ == "__main__":
    start = time.perf_counter()
    full_workload()
    end = time.perf_counter()

    print(f"Total latency: {end - start:.3f}s")

# result: Total latency: 0.484s