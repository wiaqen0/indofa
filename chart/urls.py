from django.urls import path 
from .views import chart, home
urlpatterns = [
    path('', home, name = 'chart_home'),
    path('chart/', chart, name = 'chart'),
    ]