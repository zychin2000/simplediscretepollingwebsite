from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Coral(models.Model):
    coral_image = models.ImageField(upload_to='media')
    comments = models.CharField(max_length=1000, blank=True)
    #uploader = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    # Constants in Model class
    HEALTHY = 'H'
    UNHEALTHY = 'U'
    CORAL_HEALTH_CHOICES = (
        (HEALTHY, 'Healthy'),
        (UNHEALTHY, 'Unhealthy')
    )
    coral = models.ForeignKey(Coral, on_delete=models.CASCADE)
    choice = models.CharField(max_length=1, choices=CORAL_HEALTH_CHOICES, default=HEALTHY)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
