from django.contrib import admin
from django.urls import path
from predictor import views

urlpatterns = [
    path('', views.main, name='predictor'),
    path("index1", views.index1, name='predictor1'),
    path("index2", views.index2, name='predictor2'),
]
