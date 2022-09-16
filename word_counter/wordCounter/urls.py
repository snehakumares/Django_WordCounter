from django.urls import path
from . import views

urlpatterns = [
    path('', views.wordcounter, name='wordcounter'),
    path('count', views.count, name='count'),
]