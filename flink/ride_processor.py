import json
import os
import csv

from pyflink.common import WatermarkStrategy
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import KafkaSource

# ==========================================================
# Create Flink Execution Environment
# ==========================================================

env = StreamExecutionEnvironment.get_execution_environment()

env.add_jars(
    "file:///D:/Projects/Beta_GCP_Projects_2026/Uber_Streaming_Project/jars/flink-sql-connector-kafka-3.0.1-1.18.jar"
)

env.set_parallelism(1)

# ==========================================================
# CSV File Path
# ==========================================================

csv_file = r"D:\Projects\Beta_GCP_Projects_2026\Uber_Streaming_Project\dashboard\rides.csv"

# ==========================================================
# Create CSV with Header (if missing or empty)
# ==========================================================

os.makedirs(os.path.dirname(csv_file), exist_ok=True)

if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ride_id", "location", "fare"])

# ==========================================================
# Kafka Source
# ==========================================================

source = (
    KafkaSource.builder()
    .set_bootstrap_servers("localhost:9092")
    .set_topics("uber_rides")
    .set_group_id("surge-pricing-group")
    .set_value_only_deserializer(SimpleStringSchema())
    .build()
)

stream = env.from_source(
    source,
    WatermarkStrategy.no_watermarks(),
    "Kafka Source"
)

# ==========================================================
# Process Kafka Events
# ==========================================================

def process_event(record):
    try:
        event = json.loads(record)

        ride_id = event.get("ride_id", "")
        location = event.get("location", "")
        fare = event.get("fare", "")

        with open(csv_file, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([ride_id, location, fare])

        return f"""
============================================
🚖 UBER RIDE EVENT
============================================
Ride ID   : {ride_id}
Location  : {location}
Fare      : ₹ {fare}
============================================
"""

    except Exception as e:
        return f"Error : {e}"

# ==========================================================
# Execute Stream
# ==========================================================

processed_stream = stream.map(process_event)

processed_stream.print()

env.execute("Uber Streaming Job")