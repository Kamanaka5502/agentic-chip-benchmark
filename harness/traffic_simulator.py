import asyncio
import time
from harness.metrics_collector import MetricsCollector

class TrafficSimulator:
    def __init__(self, workload, sessions=1):
        self.workload = workload
        self.sessions = sessions
        self.metrics = MetricsCollector()

    async def run_session(self, session_id):
        for _ in range(self.workload.steps):
            start = time.time()
            result = await self.workload.execute_step(session_id)
            latency = time.time() - start

            self.metrics.record(latency)

            if result and "tokens_generated" in result:
                self.metrics.total_tokens += result["tokens_generated"]

    async def run(self):
        tasks = [
            asyncio.create_task(self.run_session(i))
            for i in range(self.sessions)
        ]

        await asyncio.gather(*tasks)
        self.metrics.report()
