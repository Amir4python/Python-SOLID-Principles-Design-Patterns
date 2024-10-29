class EmailServices:
    def send_email(self,message,receiver):
        print(f'sending email to {receiver} with message {message}')

class SmsServices:
    def send_sms(self,message,receiver):
        print(f'sending sms to {receiver} with message {message}')

class NotificationService:
    def __init__(self):
        self.email_services = EmailServices()
        self.sms_services = SmsServices()

    def send_notification(self,message,receiver,method):
        if method=='email':
            self.email_services.send_email(message,receiver)
        elif method=='sms':
            self.sms_services.send_sms(message,receiver)
