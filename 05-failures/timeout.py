import random
import time
import threading


def fake_request():
    delay = random.uniform(0.1, 2.0) # non deterministic delay
    time.sleep(delay) 
    return "OK" # io bound


def run_with_timeout(timeout=1.0):
    result = {"value": None}

    def target():
        result["value"] = fake_request()

    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout) # wait for max timeout seconds

    if thread.is_alive():
        print("Request timed out")
        return None

    return result["value"]


if __name__ == "__main__":
    for i in range(5):
        print(f"Request {i+1}: {run_with_timeout()}")