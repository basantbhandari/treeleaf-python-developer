from django.db import models


class FaceEmbed(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    age = models.IntegerField()  # Age field as an integer
    emotion = models.CharField(max_length=50)  # Emotion field as a string with a maximum length of 50
    gender = models.CharField(max_length=10)  # Gender field as a string with a maximum length of 10
    timestamp = models.DateTimeField()  # Timestamp field as a DateTime

    def __str__(self):
        return f"FaceEmbed(id={self.id}, age={self.age}, emotion={self.emotion}, gender={self.gender}, timestamp={self.timestamp})"
