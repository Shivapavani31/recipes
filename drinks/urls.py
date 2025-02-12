from django.urls import path
from . import views

app_name='drinks'

urlpatterns=[
    path('Milkshakes/',views.Milkshakes,name='Milkshakes'),
    path('showmilkshakes/<int:id>',views.showmilkshakes,name='showmilkshakes'),
    path('Mojitos/',views.Mojitos,name='Mojitos'),
    path('showmojitos/<int:id>',views.showmojitos,name='showmojitos'),
    path('Juice/',views.Juice,name='Juice'),
    path('showjuice/<int:id>',views.showjuice,name='showjuice'),
    path('Softdrinks/',views.Softdrinks,name='Softdrinks'),
    path('showsoftdrinks/<int:id>',views.showsoftdrinks,name='showsoftdrinks'),
]