from django.db import models

class Data(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    bloodpressure = models.CharField(max_length=255)
    bp2 = models.CharField(max_length=255)

    def __str__(self):
        return self.bloodpressure