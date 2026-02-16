import asyncio
from harness.traffic_simulator import TrafficSimulator
from workloads.refactor_loop import RefactorLoop
from harness.adapters.mock_adapter import MockAdapter

if __name__ == "__main__":
    adapter = MockAdapter(base_latency=0.05)
    workload = RefactorLoop(adapter, steps=25)
    simulator = TrafficSimulator(workload, sessions=4)

    asyncio.run(simulator.run())
