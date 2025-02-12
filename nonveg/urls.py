from django.urls import path
from . import views

app_name='nonveg'
urlpatterns=[
    path('Chicken/',views.Chicken,name='Chicken'),
    path('showchicken/<int:id>',views.Showchicken,name='showchicken'),
    path('Meat/',views.Meat,name='Meat'),
    path('showmeat/<int:id>',views.Showmeat,name='showmeat'),
    path('Pork/',views.Pork,name='Pork'),
    path('showpork/<int:id>',views.Showpork,name='showpork'),
    path('Seafood/',views.Seafood,name='Seafood'),
    path('showseafood/<int:id>',views.Showseafood,name='showseafood'),
    path('Beef/',views.Beef,name='Beef'),
    path('showbeef/<int:id>',views.Showbeef,name='showbeef'),
]