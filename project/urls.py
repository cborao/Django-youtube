"""Project resource configuration
"""
from django.contrib import admin
from django.urls import include, path

from youtube import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('youtube.urls')),
]
