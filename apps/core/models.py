from django.db import models


class Certificate(models.Model):
    title = models.CharField(max_length=100)
    completed_on = models.DateField()
    description = models.CharField(max_length=250)
    certificate_url = models.CharField(max_length=100)

    def  __str__(self):
        return self.name
