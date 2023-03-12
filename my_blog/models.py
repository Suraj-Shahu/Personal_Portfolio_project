from django.db import models

class blog(models.Model):
    Title=models.CharField(max_length=200)
    description=models.CharField(max_length=250)
    Date=models.DateField()

    def __str__(self):
        return self.Title
    
