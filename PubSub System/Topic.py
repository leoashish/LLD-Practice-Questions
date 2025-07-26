from Subscriber import Subscriber
class Topic:
    def __init__(self, name):
        self.name = name
        self.subscribers:list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)
    
    def remove_subscriber(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def publish_message(self, message:str):
        for sub in self.subscribers:
            sub.onMessage(message)