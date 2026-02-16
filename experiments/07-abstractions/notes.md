# 07 — Abstractions

## What Is Abstraction?

Abstraction introduces layers between logic and execution.

Instead of writing direct code, we create:
- classes
- interfaces
- wrappers
- indirection

It increases structure.
It also increases distance from execution.

---

## Flat Implementation

Characteristics:
- Direct logic
- No indirection
- Fewer objects
- Fewer function calls
- Easier to trace execution

Advantages:
- Lower runtime overhead
- Clear control flow
- Easier profiling
- Fewer hidden costs

Disadvantages:
- Code duplication possible
- Harder to scale cleanly
- Harder to extend safely

---

## Abstract Implementation

Characteristics:
- Logic split into components
- Multiple objects
- Method dispatch
- Attribute lookups

Advantages:
- Clear separation of concerns
- Easier extension
- Safer modification boundaries
- Better long-term maintainability

Disadvantages:
- Extra object allocation
- More indirection
- Slight runtime overhead
- Harder to trace execution path

---

## Runtime Cost of Abstraction

Abstraction adds:

- Method call overhead
- Attribute lookup overhead
- Object instantiation cost
- Increased cognitive load

In small programs → negligible.
In tight loops → measurable.
In hot paths → critical.

---

## When Abstraction Is Premature

Abstraction is premature when:

- There is no second implementation
- There is no variation yet
- The performance path is unknown
- The code is not reused
- It hides simple logic behind structure

Premature abstraction increases:
- Complexity
- Indirection
- Debugging difficulty

Without delivering real benefit.

---

## When Abstraction Is Justified

Abstraction is justified when:

- Behavior varies
- Multiple implementations exist
- Boundaries need protection
- System is evolving
- Complexity must be contained

Good abstraction reduces risk.
Bad abstraction increases it.

---

## Execution Literacy Insight

Abstraction is not free.

Every layer adds:
- Execution cost
- Mental cost
- Debugging cost

The question is not:
"Is this clean?"

The question is:
"Is this worth it?"

---

## Core Judgment

Flat code is faster to execute.
Abstract code is safer to evolve.

Engineering is choosing which cost to pay.

Performance cost
vs
Maintenance cost

The mature engineer sees both.