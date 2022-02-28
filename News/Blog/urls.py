from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('new/<str:pk>/', views.new, name='new'),
]