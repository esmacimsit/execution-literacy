import time

N = 5_000_000  # hot path

def core(x):
    return x + 1

def clean_api(x):
    return core(x)

def layer1(x):
    return layer2(x)

def layer2(x):
    return layer3(x)

def layer3(x):
    return core(x)


def measure(label, fn, loops):
    t0 = time.perf_counter()
    x = 0
    for _ in range(loops):
        x = fn(x)
    dt = time.perf_counter() - t0
    print(f"{label:20} | loops={loops:<8} | {dt:.4f}s")


if __name__ == "__main__":
    print("=== COLD PATH (1 call) ===")
    measure("core", core, 1)
    measure("clean_api", clean_api, 1)
    measure("3 layers", layer1, 1)

    print("\n=== HOT PATH (5M calls) ===")
    measure("core", core, N)
    measure("clean_api", clean_api, N)
    measure("3 layers", layer1, N)