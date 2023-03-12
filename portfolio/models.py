from django.db import models

class Project(models.Model):
    Title=models.CharField(max_length=200)
    description=models.CharField(max_length=900)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)
