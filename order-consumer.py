import json
import uuid

from confluent_kafka import Consumer

consumer_config ={
        # Act as the starting point for a Kafka client to discover the full set of alive servers in the cluster.
        'bootstrap.servers': 'localhost:9092',
}

consumer = Consumer(consumer_config)

def delivery_report(err,msg):
    """ Called once for each message produced to indicate delivery result."""
    if err:
        print(f"❌Delivery report failed: {err}")
    else:
        print(f"✅ Delivery report succeeded: {msg.value().decode("utf-8")}")
        #print(dir(msg)) #dir-> return a list of all attributes and methods avaliable for an object
        print(f"✅ Delivery to: {msg.topic()} , Partition: {msg.partition()}, Offset: {msg.offset()}")



order = {
    "order_id": str(uuid.uuid4()),
    "user": "nana",
    "item": "Cheese pizza",
    "quantity": 2,
}

#Convert order object to Kafka data object
order_value = json.dumps(order).encode("utf-8")

consumer.consume(
    "orders",
    key=order["order_id"],
    value=order_value,
    callback = delivery_report
)

