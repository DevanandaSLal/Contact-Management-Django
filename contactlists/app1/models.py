from django.db import models

# Create your models here.
class Contacts(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    place=models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.name