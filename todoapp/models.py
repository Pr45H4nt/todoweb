from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class ListModel(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from = 'title' , unique = True , null = True)
    def __str__(self):
        return self.title

class Tasks(models.Model):
    name = models.CharField(max_length=250)
    catagory = models.ForeignKey(ListModel, on_delete= models.CASCADE)
    slug = AutoSlugField(populate_from = 'name' , unique = True , null = True)

    def __str__(self):
        return self.name
    
