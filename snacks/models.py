from django.db import models

# Create your models here.
class traditionalsnacks(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class schoolsnacks(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class timepasssnacks(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name