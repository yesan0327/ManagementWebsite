from django.urls import path
from upload import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadFile/', views.upload_file, name='upload_file'),
]
