class WorkflowContext:
    def __init__(self):
        self.data = {}
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)
        print(message)