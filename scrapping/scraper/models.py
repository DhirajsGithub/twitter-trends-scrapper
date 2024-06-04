from djongo import models
from django.utils import timezone

class TrendingTopic(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    trend1 = models.CharField(max_length=255)
    trend2 = models.CharField(max_length=255)
    trend3 = models.CharField(max_length=255)
    trend4 = models.CharField(max_length=255)
    trend5 = models.CharField(max_length=255)
    date_time = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=45)
    
    def __str__(self):
        return self.unique_id
