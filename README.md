## Run KAFKA CLI

### kafka-topics describe 
List the topics inside the server

```bash
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
````

### **kafka-console-consumer** 
*Use kafka-console-consumer to consume records from a topic.*
**It reads data from kafka topics and outputs it to standard output.**
#### To see all the the options:

```bash
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --help
```

```bash
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning
```
#### Example:
```bash
(.venv) PS C:\Users\AlanCuevas\PycharmProjects\StreamStore> docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning
The consumer rebalance protocol (KIP-848) is production-ready! Set group.protocol=consumer to try it out. See https://kafka.apache.org/documentation/#consumer_rebalance_protocol
{"order_id": "affd6f3c-722f-4aca-b04d-39089133c085", "user": "nana", "item": "Cheese pizza", "quantity": 2}
{"order_id": "1c69ec73-0dd8-4b10-b965-db2cae515f1c", "user": "nana", "item": "Cheese pizza", "quantity": 2}
{"order_id": "a0262798-41b3-4018-8c8a-87710eaaf131", "user": "nana", "item": "Cheese pizza", "quantity": 2}
{"order_id": "f5dbf806-e655-4123-a7a9-9707aac39e19", "user": "nana", "item": "Cheese pizza", "quantity": 2}
{"order_id": "227b8ce3-382e-41ba-ad7e-4e575831bb50", "user": "nana", "item": "Cheese pizza", "quantity": 2}

```
