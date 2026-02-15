# 06 — Latency Breakdown

Optimization without measurement is guessing.

---

## 1. Baseline

Baseline measures total wall-clock time.

It answers:
- How long the user waits
- Whether the system feels slow

It does NOT answer:
- Why it is slow
- Which stage dominates
- Where optimization should happen

Baseline is a black-box measurement.
The system is treated as a single unit.

---

## 2. Breakdown

Breakdown decomposes total time into components.

Typical stages:
- IO latency
- CPU latency
- Overhead

Breakdown answers:
- Where time is actually spent
- Which stage dominates
- What should be optimized

Without breakdown, optimization is blind.

---

## 3. Bottleneck

A bottleneck is the dominant latency contributor.

The slowest stage defines total performance.

Optimizing non-dominant stages produces minimal impact.

After fixing one bottleneck,
another stage becomes dominant.

Bottlenecks move.

---

## 4. CPU-bound vs IO-bound

CPU-bound:
- Dominated by computation
- Affected by algorithm complexity
- Can benefit from multiprocessing

IO-bound:
- Dominated by waiting
- Can benefit from async or concurrency
- Real external latency cannot be removed

Async hides waiting.
It does not eliminate it.

---

## 5. Overhead

Total time may not perfectly equal the sum of parts due to:

- Scheduler variability
- Context switching
- Measurement granularity
- Runtime overhead

Small discrepancies are normal.

---

## 6. Optimization Rule

1. Measure baseline.
2. Break down latency.
3. Identify bottleneck.
4. Optimize bottleneck only.
5. Re-measure.

Never optimize without measurement.