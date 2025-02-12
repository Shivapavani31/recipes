from django.contrib import admin
from .models import *
# Register your models here.
class traditionalAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class schoolAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']

class timepassAdmin(admin.ModelAdmin):
    list_display=['id','name','image','ingredients','recipe','video']   

admin.site.register(traditionalsnacks,traditionalAdmin)
admin.site.register(schoolsnacks,schoolAdmin)
admin.site.register(timepasssnacks,timepassAdmin)