from datetime import datetime


class Logger:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._buffer = []

    def log(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._buffer.append(f"[{timestamp}] {message}")

    def save(self):
        with open(self.file_path, "w") as file:
            file.write("\n".join(self._buffer))