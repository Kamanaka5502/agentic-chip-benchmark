# Agentic Chip Benchmark

A deterministic, async traffic benchmark for evaluating hardware performance under multi-turn, agentic AI coding workloads.

This project simulates realistic multi-session LLM traffic patterns (similar to Claude Code–style iterative coding agents) and measures:

- Latency (P50 / P95 / P99)
- Throughput
- Token throughput (tokens/sec)
- Multi-session concurrency behavior

The goal is to move beyond single-shot inference benchmarks and evaluate how hardware behaves under recursive, tool-augmented, multi-step agent workloads.

---

## Why This Exists

Most public AI benchmarks measure:

- Single inference latency
- Synthetic token throughput
- Static batch processing

Modern agentic systems behave differently:

- Multi-turn recursive calls
- Tool execution bursts
- Context growth across steps
- Session concurrency
- Drift over time

Hardware optimized for single-pass inference does not necessarily perform well under agent-style traffic.

This benchmark models that reality.

---

## Architecture

Workload → Traffic Simulator → Adapter → Metrics Collector

- Workloads define multi-turn traffic behavior (YAML)
- TrafficSimulator runs async concurrent sessions
- Adapters simulate or connect to model backends
- MetricsCollector computes percentiles + token throughput

---

## Metrics Collected

- Total Requests
- P50 Latency
- P95 Latency
- P99 Latency
- Mean Latency
- Total Tokens
- Tokens per Second
- Total Elapsed Time

---

## Running the Benchmark

Install:

pip install pyyaml

Run:

python run_benchmark.py

Example output:

--- Benchmark Report ---
Total Requests: 100
P50 Latency: 0.1014
P95 Latency: 0.1467
P99 Latency: 0.1508
Mean Latency: 0.1038
Total Tokens: 51057
Tokens/sec: 18550.26
Elapsed Time: 2.75 seconds

---

## Workload Profiles

Located in /workloads.

### refactor_loop.yaml
Simulates iterative code refinement across multiple turns with bounded context growth.

### debug_session.yaml
Simulates back-and-forth debugging with branching correction paths.

### tool_burst.yaml
Simulates tool-heavy workflows with frequent execution calls and higher token output.

Each profile defines:

- Steps
- Sessions
- Concurrency
- Token growth model
- Traffic profile type
- Seed for reproducibility

---

## Design Philosophy

Deterministic simulation  
Reproducible workloads  
Agent-realistic traffic patterns  
Separation of workload and adapter  
Hardware-agnostic evaluation  

This is a systems benchmark, not a model quality benchmark.

---

## Tradeoffs

- Simulated adapters do not reflect real network jitter
- Token modeling is synthetic unless connected to real backends
- YAML DSL simplifies workload representation but abstracts low-level details

However:

The architecture is extensible and adapter-driven, enabling integration with real model endpoints or on-device inference engines.

---

## Version

v1-baseline — Async multi-turn traffic simulator with percentile latency, token throughput, workload abstraction, and mock adapter.
