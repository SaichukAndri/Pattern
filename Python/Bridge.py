from abc import ABC, abstractmethod

# Абстракція
class NotificationSystem:
    def __init__(self, implementation):
        self._implementation = implementation

    def send_notification(self, message: str, recipient):
        return self._implementation.send(message, recipient)

# Реалізація
class NotificationImplementation(ABC):
    @abstractmethod
    def send(self, message: str, recipient):
        pass

class SMSNotification(NotificationImplementation):
    def send(self, message: str, phone_number: str):
        print(f"Sending SMS to {phone_number}: {message}")

class EmailNotification(NotificationImplementation):
    def send(self, message: str, email: str):
        print(f"Sending Email to {email}: {message}")

class ParentNotificationSystem(NotificationSystem):
    def notify_about_child(self, child: Child, message: str):
        for contact in child.parents_contacts:
            self.send_notification(message, contact)