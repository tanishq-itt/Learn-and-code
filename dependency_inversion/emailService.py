from messageService import MessageService

class EmailService(MessageService):
    def send(self, message):
        print("Email:", message)
