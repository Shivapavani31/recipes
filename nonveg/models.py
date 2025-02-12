from django.db import models

# Create your models here.
class chicken(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    ingrediants = models.TextField()
    description = models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class meat(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    ingrediants = models.TextField()
    description = models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class seafood(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    ingrediants = models.TextField()
    description = models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
class pork(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    ingrediants = models.TextField()
    description = models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name    
    
class beef(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    ingrediants = models.TextField()
    description = models.TextField()
    video=models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    
