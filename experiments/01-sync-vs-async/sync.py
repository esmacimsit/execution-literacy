import time

def fake_io():
    time.sleep(0.1) # Simulate a blocking I/O operation by sleeping for 0.1 seconds

def run():
    start = time.perf_counter()
    for _ in range(50): # Call the blocking I/O function 50 times sequentially
        fake_io() 
    end = time.perf_counter()
    print(f"SYNC total time: {end - start:.2f}s") # Print the total time taken for the synchronous execution

if __name__ == "__main__": 
    run()

# result is 5.2s