"""Youtube app resource configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<video_id>', views.id_info, name='id_info')
]
