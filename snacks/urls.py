from django.urls import path
from . import views

app_name='snacks'

urlpatterns=[
    path('traditional/',views.Traditionalsnacks,name='traditional'),
    path('showtraditionalsnacks/<int:id>',views.Showtraditionalsnacks,name='showtraditionalsnacks'),
    path('school/',views.Schoolsnacks,name='school'),
    path('showschoolsnacks/<int:id>',views.Showschoolsnacks,name='showschoolsnacks'),
    path('timepass/',views.Timepasssnacks,name='timepass'),
    path('showtimepasssnacks/<int:id>',views.Showtimepasssnacks,name='showtimepasssnacks'),
]