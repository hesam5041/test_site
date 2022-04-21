from django.db import models

# Create your models here.

class Work_Samples(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,max_length=30)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    body = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
