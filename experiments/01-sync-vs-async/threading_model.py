import time
import threading

def fake_io():
    time.sleep(0.1)

def run():
    threads = []
    start = time.perf_counter()

    for _ in range(50):
        t = threading.Thread(target=fake_io)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"THREAD total time: {end - start:.2f}s")

if __name__ == "__main__":
    run()
