from django.urls import path
from . import views

urlpatterns = [
  path('', views.map, name='map'),
  path('visual', views.visual, name='visual'),
  path('calculate_route', views.calculate_route)
]