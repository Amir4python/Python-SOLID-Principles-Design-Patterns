from abc import abstractmethod, ABC


class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class EmailServices(IMessageService):
    def send(self, message, receiver):
        print(f'sending email to {receiver} with message {message}')


class SmsServices(IMessageService):
    def send(self, message, receiver):
        print(f'sending sms to {receiver} with message {message}')


class NotificationService:
    def __init__(self,message_service:IMessageService):
        self.message_services = message_service


    def send_notification(self, message, receiver):
        self.message_services.send(message=message,receiver=receiver)

if __name__=="__main__":
    notification_service = NotificationService(message_service=EmailServices())
    notification_service.send_notification(message="hello",receiver="jane")