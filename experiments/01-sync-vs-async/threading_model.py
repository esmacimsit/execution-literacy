import time
import threading

def fake_io():
    time.sleep(0.1) # same simulation

def run():
    threads = [] # to track the threads we create 
    start = time.perf_counter() # Record the start time before creating threads

    for _ in range(50): 
        t = threading.Thread(target=fake_io) # thread created but not started yet
        t.start() # runs thread
        threads.append(t)

    for t in threads:
        t.join() # special thread method that waits

    end = time.perf_counter()
    print(f"THREAD total time: {end - start:.2f}s")

if __name__ == "__main__":
    run()

# result is 0.11