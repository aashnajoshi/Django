from django.db import models
from django.utils import timezone

# Create your models here (Database structures)
class form(models.Model):
    Options = {('A', 'abc'), ('B', 'bcd'), ('C', 'cde')}

    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    # img = models.ImageField(upload_to = 'data/img/')
    # fil = models.FileField(upload_to = 'data/fil/')
    choice = models.CharField(max_length=1, choices= Options, default = 'A')
    message = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name