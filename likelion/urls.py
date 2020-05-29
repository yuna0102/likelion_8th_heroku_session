from django.contrib import admin
from django.urls import path
from . import views
# .은 같은 위치
urlpatterns = [
    path('', views.index, name="index"),
]
    