from django.db import models

# Create your models here.
class sensor(models.Model):
    turbidity_value=models.FloatField(default=0)
    time=models.DateTimeField('Date accesed')
    water=models.FloatField(default=0)
    water_flow=models.FloatField(default=0)
    pH=models.FloatField(default=0)

    def __str__(self):
        return str(self.turbidity_value)

