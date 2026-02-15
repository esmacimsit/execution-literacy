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

## Concurrency vs Parallelism

**Concurrency** means multiple tasks are in progress during the same time period,
but not necessarily executing at the exact same moment.

**Parallelism** means multiple tasks are physically executing at the same time,
typically on different CPU cores.

Threading (CPU-bound):
- Concurrency: yes
- Parallelism: no (due to the GIL)

Multiprocessing:
- Concurrency: yes
- Parallelism: yes (separate processes, separate GILs, multiple cores)

## Cooperative vs Preemptive Multitasking

**Cooperative (Async):**
Tasks voluntarily yield control using `await`.
If there is no `await`, there is no concurrency.
Execution continues until a suspension point is reached.

**Preemptive (Threading):**
The OS scheduler interrupts threads automatically.
Threads can be paused at any time.
This enables concurrency but introduces race conditions.

## Multiprocessing: Windows vs macOS vs Linux

**Linux**
- Default start method: `fork`
- Child process inherits parent memory space (copy-on-write)
- Fast process startup
- No need for full re-import of main module
- Generally lower overhead

**macOS**
- Default start method: `spawn`
- Child starts fresh Python interpreter
- Main module is re-imported
- Requires `if __name__ == "__main__"` guard
- Higher startup overhead than Linux

**Windows**
- Only start method: `spawn`
- New interpreter per process
- Main module is re-executed
- `if __name__ == "__main__"` mandatory
- Highest startup overhead among the three

### Practical Implication

- `fork` → faster, lighter (Linux)
- `spawn` → safer but slower (macOS, Windows)
- CPU-bound multiprocessing scales best on Linux

## Joining vs Gathering

**Threading**
- `thread.join()`
- Blocks the main thread until the worker thread finishes.
- OS-level preemptive scheduling.

**Multiprocessing**
- `process.join()`
- Blocks the parent process until the child process exits.
- True parallel execution across multiple cores.

**Asyncio**
- `await asyncio.gather(...)`
- Suspends the current coroutine until all tasks complete.
- Cooperative scheduling (no blocking of the event loop).

### Key Difference

- `join()` → blocking (thread/process level)
- `gather()` → non-blocking suspension (event loop level)

## Additional notes

- time.perf_counter() is reliable for benchmark tests unlike time.time()
- In async code, `async` alone does not create concurrency; without an `await` suspension point, execution remains effectively synchronous.
- Optimal worker for multiprocessing is physical core number.