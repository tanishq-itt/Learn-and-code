from notifier import Notifier

class SMSNotifier(Notifier):
    def send(self, message):
        print("SMS sent:", message)
