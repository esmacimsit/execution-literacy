## hold.py — What Happens

- `tracemalloc.start()` begins tracking Python-level allocations.
- `normal_growth()` creates 1,000,000 distinct string objects.
- All objects are stored in `data`, so references remain alive.
- No object is released.

After execution:

- `current` ≈ `peak`
- Memory growth is intentional.
- This is not a leak.
- `tracemalloc.stop()` only stops tracking; it does not free memory.

## release.py — What Changes

- Memory is allocated exactly like in `hold.py`.
- `del data` removes the only external reference.
- Reference count of the list becomes 0.
- All contained string objects also drop to ref count 0.
- Objects are immediately freed by reference counting.

After execution:

- `current` drops significantly.
- `peak` does not change (it records historical maximum).
- `gc.collect()` is not required here.
- This is not a leak.

## Memory Model — Reference Counting vs GC

### Reference Counting (Primary Mechanism)

- Every object has a reference counter.
- When ref count reaches 0 → object is freed immediately.
- Fast and deterministic.
- Handles most memory cleanup in Python.

### Garbage Collector (Cyclic GC)

- Only handles circular references.
- Scans object graph to detect unreachable cycles.
- More expensive than reference counting.
- Not involved in normal object cleanup.

### Key Insight

Most memory in Python is freed by reference counting.
GC exists only to clean cycles that ref counting cannot resolve.