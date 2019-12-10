from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index', views.index, name='inde'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('contatos', views.contatos, name='contatos'),
    path('galeria', views.galeria, name='galeria'),


    

    



]