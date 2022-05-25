from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('order/',views.order,name='order'),
    path('get_centers',views.get_centers,name='get_centers'),
    path('get_flowers',views.get_flowers,name='get_flowers'),
]