from email_notifier import EmailNotifier
from sms_notifier import SMSNotifier

notifiers = [
    EmailNotifier(),
    SMSNotifier()
]

for notifier in notifiers:
    notifier.send("Hello")
