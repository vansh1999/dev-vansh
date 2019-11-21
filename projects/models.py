from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path='/img')
    sourcecode = models.URLField(max_length= 200 , default=None)

    def __str__(self):
        return self.title




