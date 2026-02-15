import random
import time


def fake_request():
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)

    if random.random() < 0.3:
        raise Exception("Network failure")

    return "OK"


def run():
    for i in range(10):
        try:
            result = fake_request()
            print(f"Request {i+1}: {result}")
        except Exception as e:
            print(f"Request {i+1} failed: {e}")


if __name__ == "__main__":
    run()