from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=60)
    #image = models.ImageField(upload_to='uploads')
    image = models.ImageField() # with upload_to and fineuploader, we get 2 files!
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
