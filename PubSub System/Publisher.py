from Topic import Topic
from ConcreteSubsriber import ConcreteSubscriber
class Publisher:
    def __init__(self, name):
        self.name = name
        self.topics:list[Topic] = []

    def register_topic(self, topic: Topic):
        self.topics.append(topic)
    
    

