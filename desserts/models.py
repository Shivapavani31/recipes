from django.db import models

# Create your models here.
class chocolate(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class cake(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class fruits(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class caramel(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class cookies(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name