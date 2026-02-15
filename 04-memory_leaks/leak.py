import tracemalloc
import time

global_store = []

def leak():
    global global_store
    for _ in range(1_000_000):
        global_store.append("x" * 100) # this causes memory leak


if __name__ == "__main__":
    tracemalloc.start()

    for i in range(5):
        leak()
        current, peak = tracemalloc.get_traced_memory()
        print(f"Iteration {i+1}")
        print(f"Current: {current / 10**6:.2f} MB")
        print(f"Peak: {peak / 10**6:.2f} MB")
        print("-" * 20)

    tracemalloc.stop()

# gc wouldnt help!!

# results:
# Iteration 1
# Current: 8.45 MB
# Peak: 8.45 MB
# --------------------
# Iteration 2
# Current: 17.13 MB
# Peak: 17.13 MB
# --------------------
# Iteration 3
# Current: 24.39 MB
# Peak: 24.39 MB
# --------------------
# Iteration 4
# Current: 34.72 MB
# Peak: 34.72 MB
# --------------------
# Iteration 5
# Current: 43.95 MB
# Peak: 43.95 MB