from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('register', views.register, name='register'),
    path('players', views.players, name='players'),
    path('registersuccess', views.registersuccess, name='registersuccess')

]


# path('XXcountdowntest1', views.XXcountdowntest1, name='XXcountdowntest1'),
