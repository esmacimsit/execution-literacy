# Execution Literacy

This repository focuses on understanding **runtime behavior, concurrency,
memory usage, latency, and failure modes** in Python.

The goal is not learning syntax or frameworks, but developing
**correct mental models and technical judgment** about how systems actually run.

All conclusions must be supported by **measurement, profiling data, or observable behavior**.

---

## Purpose

This repository exists to answer practical questions such as:

- When does code actually execute?
- What runs concurrently, and what is waiting?
- How do sync, threading, and async differ in wait management?
- When does Python become the wrong tool?
- How do failures, latency, and memory behavior affect real systems?

The emphasis is **execution**, not abstraction.

---

## Method

- Each topic is explored through **controlled experiments**
- The same workload is implemented using different execution models
- Results are evaluated using:
  - wall-clock time
  - CPU usage
  - context switches
  - memory usage
  - profiling output
- Claims without evidence are considered invalid

Statements like *“X is faster”* without context are rejected.

---

## Topics Covered

### Execution Models
Understanding how code runs under:
- synchronous execution
- threading
- asyncio

Focus:
- blocking vs yielding
- wait stacking vs wait reuse
- execution flow visibility

---

### CPU vs IO
Distinguishing computation from waiting.

Explores:
- misuse of concurrency
- async applied to CPU-bound workloads
- threads applied to IO-bound workloads

Goal:
- identify when concurrency is harmful rather than helpful

---

### GIL and Concurrency
Understanding Python’s execution constraints.

Focus:
- what the GIL actually locks
- when it is irrelevant
- when it becomes a bottleneck

Includes:
- multiprocessing
- IPC cost measurement
- thread vs process trade-offs

---

### Memory Behavior
Understanding how Python uses memory.

Explores:
- object lifecycles
- garbage collection behavior
- memory growth and leaks

Includes:
- intentional leak creation
- detection via profiling tools
- verification after fixes

---

### Failure Behavior
Studying how systems behave when things go wrong.

Includes:
- network interruption
- timeouts
- partial failures

Focus:
- failure propagation
- missing fallbacks
- system stability under stress

---

### Latency Analysis
Breaking down end-to-end latency.

Focus:
- IO time
- compute time
- wait time

Optimizations must be justified in **milliseconds**, not percentages.

---

### Abstractions and Trade-offs
Evaluating the cost of abstraction.

Includes:
- abstract vs flat implementations
- duplication vs indirection

Focus:
- performance
- risk
- maintainability

---

### AI-Assisted Code Revision
Evaluating and correcting AI-generated code.

Focus:
- race conditions
- blocking IO
- memory issues
- unnecessary abstractions

Goal:
- turn unreliable code into trustworthy systems

Each directory contains:
- minimal reproducible code
- measurement results
- concise technical notes

---

## Evaluation Standard

Progress is valid only if the following judgments become instinctive:

- “This is not async.”
- “This abstraction is premature.”
- “This will increase latency.”
- “This will cause memory pressure.”
- “This will fail under load.”

Hesitation indicates insufficient understanding.

---

## Scope

This repository intentionally avoids:
- framework tutorials
- language evangelism
- trend-driven examples

The focus is **execution behavior and decision quality**.

---

## Outcome

The expected outcome is not faster coding,
but **better technical decisions**.

Code is treated as evidence.
Judgment is the objective.
