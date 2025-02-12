from django.contrib import admin
from .models import *
# Register your models here.

class chickenadmin(admin.ModelAdmin):
    list_display = ['id','name','ingrediants','description','image','video']

class meatadmin(admin.ModelAdmin):
    list_display = ['id','name','ingrediants','description','image','video']

class seafoodadmin(admin.ModelAdmin):   
    list_display = ['id','name','ingrediants','description','image','video']

class porkadmin(admin.ModelAdmin):
    list_display = ['id','name','ingrediants','description','image','video']

class beefadmin(admin.ModelAdmin):
    list_display = ['id','name','ingrediants','description','image','video']

admin.site.register(chicken,chickenadmin)
admin.site.register(meat,meatadmin)
admin.site.register(seafood,seafoodadmin)
admin.site.register(pork,porkadmin)
admin.site.register(beef,beefadmin)