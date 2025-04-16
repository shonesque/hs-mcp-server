from typing import Callable
import sys

class Context:
    def __init__(self, request_context=None):
        self.request_context = request_context

class FastMCP:
    def __init__(self, name: str, description: str = "", lifespan: Callable = None, host: str = "0.0.0.0", port: int = 8050):
        self.name = name
        self.description = description
        self.lifespan = lifespan
        self.host = host
        self.port = port
        self.tools = []

    def tool(self):
        def decorator(func):
            self.tools.append(func)
            return func
        return decorator

    async def run_stdio_async(self):
        pass

    async def run_sse_async(self):
        pass
