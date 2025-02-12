from django.db import models

# Create your models here.
class soups(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    image = models.ImageField(upload_to='images/')
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class curries(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    image = models.ImageField(upload_to='images/')
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class quickandeasy(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    image = models.ImageField(upload_to='images/')
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name

class biryani(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    image = models.ImageField(upload_to='images/')
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class fastfood(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    image = models.ImageField(upload_to='images/')
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class staters(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    recipe = models.TextField()
    image = models.ImageField(upload_to='images/')
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name