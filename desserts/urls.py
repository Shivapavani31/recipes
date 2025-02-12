from django.urls import path
from . import views

app_name='desserts'

urlpatterns=[
    path('Cakes/',views.Cake,name='Cakes'),
    path('showcakes/<int:id>',views.Showcake,name='showcakes'),
    path('Cookies/',views.Cookies,name='Cookies'),
    path('showcookies/<int:id>',views.Showcookies,name='showcookies'),
    path('Chocolates/',views.Chocolate,name='Chocolates'),
    path('showchocolates/<int:id>',views.Showchocolate,name='showchocolates'),
    path('Fruits/',views.Fruits,name='Fruits'),
    path('showfruits/<int:id>',views.Showfruits,name='showfruits'),
    path('Caramel/',views.Caramel,name='Caramel'),
    path('showcaramel/<int:id>',views.Showcaramel,name='showcaramel'),
]
