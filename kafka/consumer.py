import sys
from confluent_kafka import Consumer

group = sys.argv[1]
c = Consumer({
    "bootstrap.servers":"localhost:9092",
    "group.id":group,
    "auto.offset.reset":"earliest",
})

c.subscribe(["demo2"])

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(msg.error())
        continue
    print(group, msg.partition(), msg.offset(), msg.key(), msg.value())