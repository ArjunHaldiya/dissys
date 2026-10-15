import sys, time
from confluent_kafka import Producer

name = sys.argv[1]
p = Producer({"bootstrap.servers": "localhost:9092"})

i = 0
try:
    while True:
        p.produce("demo2", key= f"{name}-{i}", value= f"{name}-{i}")
        p.poll(0)
        i+=1
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    p.flush()