
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('cv/', views.cv, name='mycv'),
    path('contacts/', views.hire_me, name='contacts'),
    path('success/', views.success, name='success'),
    path('projects/', views.project, name='projects'),
    # path('contact/', views.hire_me, name='contacts'),

]
