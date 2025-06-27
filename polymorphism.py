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


# Polymorphism in action - the below way of calling the same method with different notifier types is polymorphism.
# NOTE: The type of notifier is not important, the method call is what matters. If the notifier is different and the method is the same, it will work.
#  But if the method name is different, then it will not work because in the body of the for loop, we are calling the same method on all notifier types.
notifications = [SMSNotifier(), PushNotifier(), EmailNotifier()]

for notifier in notifications:
    notifier.send_notification("You've got a new message!")
