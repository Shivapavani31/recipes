from django.db import models

# Create your models here.
class milkshakes(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class mojitos(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class juice(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class smooties(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    ingredients=models.TextField()
    recipe=models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name