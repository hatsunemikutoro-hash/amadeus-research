from server.server import ServerManager, wait_server
from server.generator import Model

import asyncio

llama_path = "/home/okabe/Documentos/projects/llama.cpp/build/bin/llama-server"
model_path = "/run/media/okabe/d-mail/modelos/Llama-3.2-3B-Instruct-Q4_K_M.gguf"

server = ServerManager(llama_path, model_path)
server.start()
model = Model("Kurisu", 8080)



async def main():
    while True:
        if wait_server():
            msg_input = input("user: ")
            await model.generate(msg_input)

asyncio.run(main())
