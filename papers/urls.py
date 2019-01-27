from django.urls import path
from papers import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.all, name='all'),
]
