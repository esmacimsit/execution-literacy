import tracemalloc # trace memory allocations in Python
import time

def normal_growth():
    data = []
    for _ in range(1_000_000):
        data.append("x" * 100)
    return data


if __name__ == "__main__":
    tracemalloc.start() # start tracing memory allocations

    start = time.perf_counter()
    data = normal_growth()
    end = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    print(f"Time: {end - start:.2f}s")
    print(f"Current memory: {current / 10**6:.2f} MB")
    print(f"Peak memory: {peak / 10**6:.2f} MB")

    tracemalloc.stop()

# results:
# Time: 0.13s
# Current memory: 8.45 MB
# Peak memory: 8.45 MB