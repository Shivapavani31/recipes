from django.contrib import admin
from .models import *
# Register your models here.
class idlyAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class dosaAdmin(admin.ModelAdmin):  
    list_display=['id','name','image','ingredients','recipe','video']

class pohaAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class upmaAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class puriAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

admin.site.register(idly,idlyAdmin)
admin.site.register(dosa,dosaAdmin)
admin.site.register(poha,pohaAdmin)
admin.site.register(upma,upmaAdmin)
admin.site.register(puri,puriAdmin)
