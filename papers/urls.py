from django.urls import path
from papers import views

urlpatterns = [
    path('API/', views.index, name='index'),
    path('inputcode/', views.inputcode, name='inputcode'),
    path('outputcode/', views.outputcode, name='outputcode'),
    path('function/', views.function, name='function'),
    path('2005/', views.time_2005, name='time'),
    path('2006/', views.time_2006, name='time'),
    path('2007/', views.time_2007, name='time'),
    path('2008/', views.time_2008, name='time'),
    path('2009/', views.time_2009, name='time'),
    path('2010/', views.time_2010, name='time'),
    path('2011/', views.time_2011, name='time'),
    path('2012/', views.time_2012, name='time'),
    path('2013/', views.time_2013, name='time'),
    path('2014/', views.time_2014, name='time'),
    path('2015/', views.time_2015, name='time'),
    path('2016/', views.time_2016, name='time'),
    path('2017/', views.time_2017, name='time'),
    path('2018/', views.time_2018, name='time'),
    path('2019/', views.time_2019, name='time'),
    path('ASE/', views.ase, name='ase'),
    path('all/', views.all, name='all'),
    path('get_keywords/', views.get_keywords, name='get_keywords'),
    path('result/', views.result, name='result'),

]
