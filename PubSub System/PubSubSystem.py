from Publisher import Publisher
from Subscriber import Subscriber
from Topic import Topic
class PubSubSystem:
    def __init__(self):
        self.publishers: list[Publisher] = []
        self.subscribers:list[Subscriber]= []
        
    def register_publisher(self, publisher: Publisher):
        self.publishers.append(publisher)

    def register_topic(self, topic: Topic, publisher: Publisher):
        publisher.topics.append(topic)
    
    def register_subscriber(self, topic:Topic, subscriber: Subscriber):
        topic.subscribe(subscriber)

    def publish_message(self, topic: Topic , message: str):
        topic.publish_message(message)