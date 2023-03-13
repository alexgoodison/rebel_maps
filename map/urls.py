from django.urls import path
from . import views

urlpatterns = [
  path('', views.map, name='map'),
  path('calculate_route', views.calculate_route),
]