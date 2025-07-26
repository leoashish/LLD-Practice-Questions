from abc import abstractmethod


class Subscriber:
    
    @abstractmethod
    def onMessage(self, message:str):
        pass