from django.db import models

class Image(models.Model):

    title = models.CharField(max_length=60)
    uuid = models.CharField(max_length=60, blank=True, null=False)
    #image = models.ImageField() # with upload_to and fineuploader, we get 2 files!
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

