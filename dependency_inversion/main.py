from emailService import EmailService
from user import UserApp

service = EmailService()
app = UserApp(service)

app.notify("Welcome user")
