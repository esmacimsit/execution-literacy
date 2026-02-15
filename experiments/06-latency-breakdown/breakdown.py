import time
from workload import io_work, cpu_work

if __name__ == "__main__":
    total_start = time.perf_counter()

    io_start = time.perf_counter()
    io_work()
    io_end = time.perf_counter()

    cpu_start = time.perf_counter()
    cpu_work()
    cpu_end = time.perf_counter()

    total_end = time.perf_counter()

    print(f"IO latency:  {io_end - io_start:.3f}s")
    print(f"CPU latency: {cpu_end - cpu_start:.3f}s")
    print(f"Total:       {total_end - total_start:.3f}s")

# results:
# IO latency:  0.302s
# CPU latency: 0.170s
# Total:       0.472s