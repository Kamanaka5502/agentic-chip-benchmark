# Agentic Chip Benchmark
## Design Document

## Objective

- Measure performance of public compute hardware under multi-session, multi-turn agentic AI coding workloads.
- Unlike generic throughput tests that optimize for raw speed, this benchmark evaluates replay integrity and constraint stability under concurrency.
- Token processing rate
- Replay determinism under fixed workload constraints

The goal is to simulate Claude Code–style iterative refactor sessions under realistic concurrency pressure.
Workload Model

## Evaluation Methodology
- Fixed hardware configuration per run
- N repeated runs per chip
- Report median and tail latency (P95 / P99)
- Record variance across runs
- All workload seeds fixed for reproducibility

## Each session simulates:
- Multi-step refactor loop
- Stateful progression
- Deterministic execution pattern
- Configurable latency model (mock or hardware-backed adapter)

Multiple sessions execute concurrently to approximate real-world coding agent pressure.

## Metrics Captured
- End-to-end latency distribution
- Requests per second
- Token throughput
- Latency variance under concurrency

## Determinism Model
- Fixed workload definitions
- Controlled concurrency parameters
- Reproducible session graphs
- Adapter abstraction layer for hardware substitution

## Tradeoffs
- MockAdapter enables deterministic replay but does not capture real inference jitter.
- Async concurrency models user-level parallelism but not GPU kernel scheduling contention.
- Token throughput is simulated unless backed by a real inference adapter.

## Future Extensions
- Real inference adapter integration
- Cross-chip comparative runs
- Replay integrity scoring
- Deterministic boundary enforcement validation
