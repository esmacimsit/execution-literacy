# Notes on timing

`fake_io()` simulates an IO-bound wait, not real disk or network IO.

`time.sleep(0.1)` means:
- wait *at least* 0.1 seconds
- actual wake-up may be slightly later

The same workload was repeated 50 times.

# Worker analogy

Sync: one worker does all tasks sequentially.
Each wait blocks the next task.

Thread: multiple workers start at the same time.
Workers do not wait for each other.
Only the owner (main thread) waits before closing.

Async: a single worker switches tasks while waiting.
No extra workers are created.
Waiting time is reused instead of stacked.

# Formulation

- SYNC   ≈ sum(wait_i)
- THREAD ≈ max(wait_i) + overhead
- ASYNC  ≈ max(wait_i) + smaller overhead

# Detecting Sync vs Thread vs Async

## Async
Indicators:
- `async def`
- `await`
- `asyncio.run`
- `asyncio.gather` (event loop)

## Thread
Indicators:
- `import threading`
- `threading.Thread(...)`
- `start()`
- `join()` (OS scheduler)

## Sync
Indicators:
- No `async` / `await`
- No `threading`
- Blocking calls (`time.sleep`, blocking IO)
- Direct function calls in loops

# Extra intuition

`join` is like a salaried worker on fixed hours:
after work starts, no new tasks are accepted until the shift ends.

`gather` is like a freelancer:
even while waiting on a task, they keep checking for new work.
This constant readiness is the event loop.
