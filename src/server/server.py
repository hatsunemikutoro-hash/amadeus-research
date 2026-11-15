import subprocess
import atexit
import requests
import time

llama_path = "/home/okabe/Documentos/projects/llama.cpp/build/bin/llama-server"
model_path = "/run/media/okabe/d-mail/modelos/Llama-3.2-3B-Instruct-Q4_K_M.gguf"

def wait_server():
    for _ in range(120):
        try:
            r = requests.get("http://127.0.0.1:8080/health", timeout=2)
            if (r.status_code == 200):
                return True
        except:
            continue
        

class ServerManager:
    def __init__(self, llama, model, port=8080) -> None:
        self.port = port
        self.server = None
        self.args = [
            llama,
            "-m", model,
            "-ngl", "99",
            "-c", "8192",
            "--jinja",
            "-fa", "on",
            "--no-reasoning-preserve",
            "--reasoning-budget", "0",
            "--host", "127.0.0.1",
            "--port", str(self.port),
            
        ]

    def start(self):
        print("Iniciando servidor")
        self.server = subprocess.Popen(self.args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        atexit.register(self.stop)
        
    def stop(self):
        if self.server:
            self.server.terminate()
            


