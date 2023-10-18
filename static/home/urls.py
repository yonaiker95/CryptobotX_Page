from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('update/', views.about, name='update'),
]
