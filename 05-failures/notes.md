## Failure Engineering Overview

### unprotected.py
- Exception is not caught.
- A single failure terminates the entire program.
- No isolation between operations.
- Fragile design.

---

### protected.py
- Exception is caught locally.
- Failure is isolated per request.
- Program continues executing.
- Basic resilience.

---

### fallback.py
- Primary failure triggers alternative path.
- System degrades gracefully.
- No retry or recovery logic.
- If primary keeps failing → fallback is always used.

---

### try / except
- `raise` interrupts execution flow.
- Python jumps to the nearest matching `except`.
- Execution continues after the handler.

Failure scope depends on placement:
- Try inside loop → only that iteration fails.
- Try outside loop → entire loop stops on first error.

---

### Circuit Breaker
- Failures are counted.
- Threshold exceeded → circuit opens.
- Primary is skipped.
- System routes directly to fallback.

Purpose:
- Prevent latency amplification.
- Avoid repeated wasted work.
- Protect system stability.

States:
- Closed → normal execution.
- Open → primary disabled.
- Half-open → test recovery.

---

### timeout.py
- Limits waiting time using `join(timeout)`.
- If worker exceeds limit → timeout declared.
- Execution continues.
- Worker is NOT terminated.

Risk:
- Background work may continue.
- Accumulated timeouts waste resources.

Timeout ≠ cancellation.

---

### Retry
- Re-attempts a failed operation.
- Stops early if success occurs.
- Limited by `max_attempts`.
- Sleeps between attempts.

Used for:
- Transient failures
- Temporary instability

Risk:
- Blind retry can amplify load.
- No backoff → retry storm.
- Not suitable for permanent failures.

Retry attempts recovery.
It does not guarantee stability.

---

### Backoff
- Adds delay between retries.
- Reduces pressure on failing systems.
- Often exponential.
- May include jitter to prevent synchronized retry spikes.

---

## Failure Strategy Levels

1. Unprotected → crash
2. Protected → isolate
3. Fallback → degrade
4. Retry → attempt recovery
5. Circuit breaker → stop repeated failure
6. Timeout → bound waiting time

Failure is inevitable.
System collapse is optional.