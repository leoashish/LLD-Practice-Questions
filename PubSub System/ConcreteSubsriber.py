from typing import override
from Subscriber import Subscriber

class ConcreteSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    @override
    def onMessage(self, message): # type: ignore
        print(f"Subscriber {self.name} , Message: {message}")
        