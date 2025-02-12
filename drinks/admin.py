from django.contrib import admin
from .models import *
# Register your models here.

class milkshakesAdmin(admin.ModelAdmin):
    list_display=['name','image','ingredients','recipe','video']

class mojitosAdmin(admin.ModelAdmin):
    list_display=['name','image','ingredients','recipe','video']

class juiceAdmin(admin.ModelAdmin):
    list_display=['name','image','ingredients','recipe','video']

class smootiesAdmin(admin.ModelAdmin):
    list_display=['name','image','ingredients','recipe','video']

admin.site.register(milkshakes,milkshakesAdmin)
admin.site.register(mojitos,mojitosAdmin)
admin.site.register(juice,juiceAdmin)
admin.site.register(smooties,smootiesAdmin)