from django.db import models


class Result(models.Model):
    user1 = models.CharField(max_length=255)
    quality_score = models.IntegerField()
    latency_score = models.IntegerField()
    duration_score = models.IntegerField()
    efficiency_score = models.IntegerField()
    disturbances_score = models.IntegerField()
    medication_score = models.IntegerField()
    daytime_discomfort_score = models.IntegerField()
    total_score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1} - {self.date.strftime('%Y-%m-%d')}"
