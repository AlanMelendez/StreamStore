import json
import uuid

from confluent_kafka import Consumer

consumer_config ={
    'bootstrap.servers': 'localhost:9092', #Connect to server
    'group.id': "order-tracker", # Name that identifies the consumer group this consumer belongs to.
    'auto.offset.reset': 'earliest' # It takes the first message in the queue ex. (1,2,3,4) take "1" first. (earliest,latest,by_duration:<duration>,none)
}

consumer = Consumer(consumer_config)

topics_to_subscribe = ["orders"] # [orders,payments] and so on.

consumer.subscribe(topics=topics_to_subscribe)

print("🟢 Consumer is running and subscribed to topics ${topics_to_subscribe[0]}")
try:
    while True:
        msg = consumer.poll(timeout=1.0) # Poll asks kafka for messages meanwhile "timeout" waits up to 1 second for a message.
        if msg is None:
            continue
        if msg.error():
            print("❌ Consumer is error: {}".format(msg.error()))
            continue
        value = msg.value().decode("utf-8")
        json_value = json.loads(value) # Convert json to python dictionary.


        print(f"📦 Received order: {json_value['quantity']} x {json_value['item']} from user: {json_value['user']}")
except KeyboardInterrupt: # Manual stop or crash
    print("\n🔴 Stopping the consumer")
finally:
    consumer.close() # Close connection securely and offsets are commited and partition assignments are revoked.
