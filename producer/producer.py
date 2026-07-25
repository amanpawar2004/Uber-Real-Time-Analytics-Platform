from kafka import KafkaProducer
import json
import random
import time

from datetime import datetime

TOPIC = "uber_rides"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

locations = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai"
]

while True:

    ride_event = {
        "ride_id": f"R{random.randint(1000,9999)}",
        "driver_id": f"D{random.randint(1,500)}",
        "location": random.choice(locations),
        "fare": random.randint(100,500),
        "timestamp": datetime.utcnow().isoformat()
    }

    producer.send(TOPIC, ride_event)

    print("Sent:",ride_event)

    time.sleep(0.05)