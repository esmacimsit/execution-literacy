## GIL

The Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time.

In synchronous, single-threaded execution, the GIL is effectively idle because there is no contention.
It becomes relevant only when multiple threads are introduced, preventing true parallel execution for CPU-bound workloads.

As a result, threading does not improve performance for CPU-bound tasks in Python.

## Additional notes

- time.perf_counter() is reliable for benchmark tests unlike time.time()