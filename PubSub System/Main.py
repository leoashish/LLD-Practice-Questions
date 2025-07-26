from PubSubSystem import PubSubSystem
from Publisher import Publisher
from ConcreteSubsriber import ConcreteSubscriber
from Topic import Topic

def main():
    # Create PubSub system
    pubsub = PubSubSystem()

    # Create publishers
    publisher1 = Publisher("Publisher1")
    publisher2 = Publisher("Publisher2")

    # Create subscribers
    subscriber1 = ConcreteSubscriber("Subscriber1")
    subscriber2 = ConcreteSubscriber("Subscriber2")
    subscriber3 = ConcreteSubscriber("Subscriber3")

    topic1 = Topic("news")
    topic2 = Topic("sports")
    topic = Topic("weather")

    topic1.subscribe(subscriber1)
    topic1.subscribe(subscriber2)
    topic1.subscribe(subscriber3)
    
    topic2.subscribe(subscriber1)
    # Subscribers subscribe to topics
    
    pubsub.register_publisher(publisher1)
    pubsub.register_publisher(publisher2)   

    pubsub.publish_message(topic1, "Breaking News!")
    pubsub.publish_message(topic2, "Sports Update!")

if __name__ == "__main__":
    main()
