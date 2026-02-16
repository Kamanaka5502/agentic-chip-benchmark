import asyncio
import random
from harness.model_adapter import ModelAdapter

class MockAdapter(ModelAdapter):
    def __init__(self, base_latency=0.05):
        self.base_latency = base_latency

    async def execute(self, prompt: str) -> dict:
        simulated_latency = self.base_latency + random.uniform(0.01, 0.1)
        await asyncio.sleep(simulated_latency)

        tokens = random.randint(200, 800)

        return {
            "status": "ok",
            "tokens_generated": tokens,
            "latency": simulated_latency
        }
