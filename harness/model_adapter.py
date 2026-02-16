class ModelAdapter:
    async def execute(self, prompt: str) -> dict:
        raise NotImplementedError("ModelAdapter subclasses must implement execute()")
