from django.urls import path
from . import views

urlpatterns = [
    path('home', views.landingpage, name='landingpage'),
    path('XXcountdowntest1', views.XXcountdowntest1, name='XXcountdowntest1'),
]
