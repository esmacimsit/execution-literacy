## GIL

The Global Interpreter Lock (GIL) ensures that only one thread executes Python bytecode at a time.

In synchronous, single-threaded execution, the GIL is effectively idle because there is no contention.
It becomes relevant only when multiple threads are introduced, preventing true parallel execution for CPU-bound workloads.

As a result, threading does not improve performance for CPU-bound tasks in Python.

## NumPy and the GIL

The Global Interpreter Lock (GIL) prevents multiple threads from executing Python bytecode at the same time.

However, many scientific libraries such as NumPy execute heavy computations in C, outside of the Python interpreter.

During long-running C-level operations (e.g. matrix multiplication), NumPy releases the GIL.
This allows other Python threads to run in parallel while the C code continues executing.

As a result:

- Pure Python CPU-bound loops do not benefit from threading.
- C-backed numerical operations (e.g. `np.dot`) may benefit from threading.
- True parallelism becomes possible when computation happens outside the Python interpreter.

Important distinction:

CPU-bound Python code ≠ CPU-bound C-backed code.

Threading fails in the first case due to the GIL,
but may scale in the second case if the GIL is released.

## Single Thread vs CPU Cores

In CPU-bound single-threaded execution, Python runs on only one core.

Core count alone does not speed up execution.  
Performance depends on single-core speed (clock, IPC, cache), not total cores.

An 8-core machine will not run a single-threaded workload 8× faster.
It will use one core while the others remain idle.

True multi-core utilization requires multiprocessing, not threading.



## Additional notes

- time.perf_counter() is reliable for benchmark tests unlike time.time()