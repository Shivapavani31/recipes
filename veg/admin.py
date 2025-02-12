from django.contrib import admin
from .models import *
# Register your models here.

class soupsadmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','recipe','image','video']

class curriesadmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','recipe','image','video']

class quickandeasyadmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','recipe','image','video']

class biryaniadmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','recipe','image','video']

class fastfoodadmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','recipe','image','video']

class statersadmin(admin.ModelAdmin):    
    list_display = ['id','name','ingredients','recipe','image','video']

admin.site.register(soups,soupsadmin)
admin.site.register(curries,curriesadmin)   
admin.site.register(quickandeasy,quickandeasyadmin)
admin.site.register(biryani,biryaniadmin)
admin.site.register(fastfood,fastfoodadmin)
admin.site.register(staters,statersadmin)
