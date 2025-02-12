from django.urls import path
from . import views

app_name='ourrecipe1'

urlpatterns=[
    path('',views.home,name='home'),
    path('veg/',views.veg,name='veg'),
    path('nonveg/',views.nonveg,name='nonveg'),
    path('dessert/',views.dessert,name='dessert'),
    path('drinks/',views.drinks,name='drinks'),
    path('snacks/',views.snacks,name='snacks'),
    path('tiffins/',views.tiffins,name='tiffins'),
    path('calories/',views.calories,name='calories')
]