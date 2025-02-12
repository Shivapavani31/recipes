from django.contrib import admin
from .models import *

# Register your models here.

class chocolateAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class cakeAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class fruitsAdmin(admin.ModelAdmin):    
    list_display=['id','name','image','ingredients','recipe','video']

class caramelAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']   

class cookiesAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

admin.site.register(chocolate,chocolateAdmin)
admin.site.register(cake,cakeAdmin)
admin.site.register(fruits,fruitsAdmin)
admin.site.register(caramel,caramelAdmin)
admin.site.register(cookies,cookiesAdmin)

