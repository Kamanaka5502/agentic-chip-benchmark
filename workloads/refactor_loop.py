class RefactorLoop:
    def __init__(self, adapter, steps=20):
        self.adapter = adapter
        self.steps = steps

    async def execute_step(self, session_id):
        prompt = f"Refactor session {session_id}"
        result = await self.adapter.execute(prompt)
        return result
