class UserApp:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)
