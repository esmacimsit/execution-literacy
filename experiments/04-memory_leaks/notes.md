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

---

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

---

## leak.py — What Actually Leaks

- `global_store` lives in global scope.
- Each call to `leak()` appends 1,000,000 new string objects.
- No references are removed.
- Reference counts never reach zero.
- Memory grows on every iteration.

This is not a GC failure.

Objects are still reachable through `global_store`,
so neither reference counting nor GC can free them.

---

## Why GC Does Nothing Here

- There is no circular reference.
- All objects are strongly referenced.
- `gc.collect()` cannot free reachable objects.

This is an application-level leak caused by unbounded state retention.

---

## Memory Model — Reference Counting vs GC

### Reference Counting (Primary Mechanism)

- Every object has a reference counter.
- When ref count reaches 0 → object is freed immediately.
- Fast and deterministic.
- Handles most memory cleanup in Python.

### Garbage Collector (Cyclic GC)

- Only handles circular references.
- Scans the object graph to detect unreachable cycles.
- More expensive than reference counting.
- Not involved in normal object cleanup.

### Cycles Without GC

If circular references exist and the cyclic GC is disabled,
those objects will not be freed by reference counting.

In that case, memory can grow even though the objects are
no longer reachable from the program logic.

This is uncommon in production, but possible.

---

## When Memory Growth Is Not a Leak

Memory increase does not automatically mean a leak.

Common causes in GenAI systems:

- Model KV cache growth during long sequences
- Streaming token buffers not flushed
- In-memory embedding indexes
- Allocator caching (Python, MLX, Torch)
- Session state retained by design

In these cases:

- Objects are still referenced.
- Reference count never reaches zero.
- GC has nothing to clean.

---

## Additional Notes

- RSS = OS-level resident memory.
- `tracemalloc` tracks Python-level allocations only.
- Most memory in Python is freed by reference counting.
- GC exists only to clean cycles that reference counting cannot resolve.