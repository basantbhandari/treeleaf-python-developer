from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

# Configuration for Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of possible emotions and genders
emotions = ['happy', 'sad', 'angry', 'surprised', 'neutral']
genders = ['male', 'female', 'other']


def generate_random_data():
    return {
        'id': random.randint(1, 1000000),  # Generate a random id
        'age': random.randint(1, 100),  # Generate a random age between 1 and 100
        'emotion': random.choice(emotions),  # Randomly select an emotion
        'gender': random.choice(genders),  # Randomly select a gender
        'timestamp': datetime.now().isoformat()  # Current timestamp
    }


# Produce random data to Kafka topic
while True:
    data = generate_random_data()
    producer.send('face.embed.data', value=data)
    print(f"Produced: {data}")
    time.sleep(5)  # Sleep for 5 seconds before sending the next message
