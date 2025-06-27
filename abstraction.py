from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class SMSNotifier(Notifier):
    def send_notification(self, message: str):
        print(f"Sending SMS: {message}")


class PushNotifier(Notifier):
    def send_notification(self, message: str):
        print(f"Sending Push Notification: {message}")


class EmailNotifier(Notifier):
    def send_notification(self, message: str):
        print(f"Sending Email: {message}")


sms_notification = SMSNotifier()
sms_notification.send_notification("Hello Abhinav")
push_notification = PushNotifier()
push_notification.send_notification("Hello Abhinav")
email_notification = EmailNotifier()
email_notification.send_notification("Hello Abhinav")
