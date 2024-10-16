from django.db import models

# Create your models here (Database structures)
class form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    message = models.TextField()
    
    def __str__(self):
        return self.name