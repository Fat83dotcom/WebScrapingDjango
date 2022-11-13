from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('cnn/', views.coreCnn, name='cnn'),
    path('g1/', views.coreG1, name='g1'),
    path('uol/', views.coreUOL, name='uol'),
]