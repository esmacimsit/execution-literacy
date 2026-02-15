import random
import time


def unstable_call():
    if random.random() < 0.7:
        raise Exception("Temporary failure")
    return "Success" # non deterministic


def retry(max_attempts=3):
    for attempt in range(max_attempts):
        try:
            return unstable_call()
        except Exception as e:
            print(f"Attempt {attempt+1} failed")
            time.sleep(0.2)
    return "Failed after retries"


if __name__ == "__main__":
    print(retry())