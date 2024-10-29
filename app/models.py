from django.db import models
from django.utils import timezone

# Create your models here. (Database structures)
class Form(models.Model):
    OPTIONS = [(1, 'Abc'), (2, 'Bcd'), (3, 'Cde')]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique= True)
    dob = models.DateField()
    img = models.ImageField(upload_to='img/', null=True, default=None)
    doc = models.FileField(upload_to='doc/', null=True, default=None)
    choice = models.IntegerField(choices=OPTIONS, default=1)
    message = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Forms" # Changes the name of the table in the admin panel

    def __str__(self):
        return f"{self.name}, {self.email}, {self.dob}, {self.choice}, {self.message}, {self.date_added}"