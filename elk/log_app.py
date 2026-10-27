import socket
import datetime
import random
import time


HOST = "localhost"
PORT = 5000
choices = {"INFO" : ["logged in", "searching"], "WARN" : ["slow response", "high disk usage"], "ERROR":["db timeout","payment failed"]}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST,PORT))
    while True:
        level=random.choice(list(choices))
        text=random.choice(choices[level])
        message = f"{datetime.datetime.now().isoformat(timespec='seconds')} {level} user {random.randint(1,100)} {text}\n"
        client.sendall(message.encode("utf-8"))
        print(message, end="")
        time.sleep(1)
        