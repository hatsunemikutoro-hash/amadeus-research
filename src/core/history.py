import queue

class History:
    def __init__(self, MAXSIZE, prompt, debug=False):
        self.debug = debug
        self.history = []
        self.maxsize = MAXSIZE
        self.history.append({ "role": "system", "content": prompt})

    def add_msg(self, user, msg: str):
        self.history.append({"role": user, "content": msg})
        if self.debug:
            print(self.history)
        
        if len(self.history) + 1 > self.maxsize:
            self.prune()

    def prune(self):
        self.history.pop(1)
