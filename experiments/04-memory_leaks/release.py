import tracemalloc
import time
import gc

def allocate():
    data = []
    for _ in range(1_000_000):
        data.append("x" * 100)
    return data


if __name__ == "__main__":
    tracemalloc.start()
    data = allocate()      
    # just two lines different from hold.py
    del data # remove reference to data, allowing it to be garbage collected
    gc.collect() # not necessary, but can help to free memory immediately

    current, peak = tracemalloc.get_traced_memory()

    print(f"Current memory after delete: {current / 10**6:.2f} MB")
    print(f"Peak memory: {peak / 10**6:.2f} MB")

    tracemalloc.stop()

# results:
# Current memory after delete: 0.00 MB
# Peak memory: 8.45 MB