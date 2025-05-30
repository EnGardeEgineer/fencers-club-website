from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('membership/', views.membership, name='membership'),
    path('programs/', views.programs, name='programs'),
    path('coaches/', views.coaches, name='coaches'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 