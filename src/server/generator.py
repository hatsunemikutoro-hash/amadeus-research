from openai import AsyncOpenAI
from core.history import History
import asyncio

class Model:
    def __init__(self,name, port, historic=True):
        self.name = name
        self.port = port

        # historico de msg ta aqui
        self.history = History(6, "você é makise kurisu", False)
        
        self.client = AsyncOpenAI(
            base_url=f"http://localhost:{self.port}/v1",
            api_key="no-key-required",
        )

    # funcao que gera msg
    async def generate(self, msg: str):
        self.history.add_msg("user", msg)
        
        stream = await self.client.chat.completions.create(
            model="local-model",
            messages=self.history.history,
            stream=True,
        )

        print(f"{self.name}: ", end="")
        parts = []
        
        async for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                parts.append(content)
                print(content, end="", flush=True)
        
        text_complete = "".join(parts)
        self.history.add_msg("assistant", text_complete)
        
        print()
