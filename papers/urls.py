from django.urls import path
from papers import views

urlpatterns = [
    path('API/', views.index, name='index'),
    path('inputcode/', views.inputcode, name='inputcode'),
    path('outputcode/', views.outputcode, name='outputcode'),
    path('function/', views.function, name='function'),
    path('2013/', views.time, name='time'),
    path('ASE/', views.ase, name='ase'),
    path('all/', views.all, name='all'),
    path('get_keywords/', views.get_keywords, name='get_keywords'),
    path('result/', views.result, name='result'),


]
