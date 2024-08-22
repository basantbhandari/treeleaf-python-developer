from django.core.management.base import BaseCommand
from kafka import KafkaConsumer
import json
from datetime import datetime

from kafka_app.models import FaceEmbed


class Command(BaseCommand):
    help = 'Consumes messages from Kafka and stores them in the FaceEmbed model'

    def handle(self, *args, **kwargs):
        consumer = KafkaConsumer(
            'face.embed.data',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            group_id='face_embed_group'
        )

        print("Listening for messages on 'face.embed.data'...")

        for message in consumer:
            data = message.value
            print(f"Consumed: {data}")

            # Convert the timestamp to a datetime object
            timestamp = datetime.fromisoformat(data['timestamp'])

            # Save the data to the FaceEmbed model
            face_embed = FaceEmbed(
                id=data['id'],
                age=data['age'],
                emotion=data['emotion'],
                gender=data['gender'],
                timestamp=timestamp
            )
            face_embed.save()
            print(f"Saved: {face_embed}")
