from django.urls import path
from . import views

app_name='veg'

urlpatterns=[   
    path('soups/',views.Soups,name='soups'),
    path('showsoups/<int:id>',views.showsoups,name='showsoups'),
    path('curries/',views.Curries,name='curries'),
    path('showcurries/<int:id>',views.showcurries,name='showcurries'),
    path('quickandeasy/',views.Quickandeasy,name='quickandeasy'),
    path('showquickandeasy/<int:id>',views.showquickandeasy,name='showquickandeasy'),
    path('biryani/',views.Biryani,name='biryani'),
    path('showbiryani/<int:id>',views.showbiryani,name='showbiryani'),
    path('fastfood/',views.Fastfood,name='fastfood'),
    path('showfastfood/<int:id>',views.showfastfood,name='showfastfood'),
    path('staters/',views.Staters,name='staters'),
    path('showstaters/<int:id>',views.showstaters,name='showstaters'),
]