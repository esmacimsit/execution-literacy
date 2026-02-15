import random

def primary_model():
    if random.random() < 0.5: # non deterministic failure
        raise Exception("Primary model unavailable")
    return "Primary response"


def fallback_model():
    return "Fallback response"


def run():
    try:
        return primary_model()
    except Exception:
        return fallback_model()


if __name__ == "__main__":
    for i in range(5):
        print(run())