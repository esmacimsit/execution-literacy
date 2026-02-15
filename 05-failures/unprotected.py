import random
import time


def fake_request():
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)

    if random.random() < 0.3:
        raise Exception("Network failure") # This will cause the program to crash if not handled

    return "OK"


def run():
    for i in range(10):
        result = fake_request()
        print(f"Request {i+1}: {result}")


if __name__ == "__main__":
    run()