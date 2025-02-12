from django.urls import path
from . import views

app_name='tiffins'

urlpatterns=[
    path('idly/',views.Idly,name='idly'),
    path('showidly/<int:id>',views.Showidly,name='showidly'),   
    path('dosa/',views.Dosa,name='dosa'),
    path('showdosa/<int:id>',views.Showdosa,name='showdosa'),
    path('puri/',views.Puri,name='puri'),
    path('showpuri/<int:id>',views.Showpuri,name='showpuri'),
    path('upma/',views.Upma,name='upma'),
    path('showupma/<int:id>',views.Showupma,name='showupma'),
    path('poha/',views.Poha,name='poha'),
    path('showpoha/<int:id>',views.Showpoha,name='showpoha'),
]
