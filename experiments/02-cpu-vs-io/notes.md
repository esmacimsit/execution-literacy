## CPU-bound

In CPU-bound tests, synchronous execution is used as the baseline since it already
runs on a single thread. Adding threads would introduce overhead without providing
parallel speedup, and is therefore intentionally omitted.

**Definition:**  
A task is **CPU-bound** when its runtime is limited by how fast the **CPU can compute**, not by waiting.

**CPU:**  
The actual processor executing instructions (calculations, loops, branches).

**Signal:**  
High CPU usage, little or no waiting.

**Analogy:**  
Thinking hard about a problem — speed depends on brain power.

---

## IO-bound

In IO-bound tests, asynchronous execution is used as the primary model to
overlap waiting time. The synchronous version serves as a baseline where
blocking calls accumulate latency. Threading is intentionally omitted to
isolate the effects of event-loop scheduling without introducing extra
synchronization overhead.

**Definition:**  
A task is **IO-bound** when its runtime is limited by **waiting for input/output**, not computation.

**IO:**  
Interaction outside the CPU: disk, network, database, filesystem, timers.

**Signal:**  
Low CPU usage, most time spent waiting.

**Analogy:**  
Waiting for a delivery — nothing to do until it arrives.

## GIL (Global Interpreter Lock)

**What it is:**  
A lock in **CPython** that allows only **one thread** to execute Python bytecode at a time.

**Why it matters:**  
- **CPU-bound + threads:** usually **no real speedup** (threads take turns holding the lock)  
- **IO-bound + threads:** can help, because threads often **release the GIL while waiting** (disk/network)

**Analogy:**  
Many workers, but only **one pen** — only the worker holding the pen can write.

---

## Additonal notes

- CPU heavy work -> C,C++ (because of GIL), IO heavy work -> Python
- CPU latency may vary between runs due to OS scheduling, background workloads, CPU frequency scaling, and cache effects.
- async pays overhead per task
- compute heavy work naturally works like sync