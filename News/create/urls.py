from django.urls import path, include
from . import views
from .views import index , LoginView

urlpatterns = [
    path('', index.as_view(), name ='index'),
    path('login/',LoginView.as_view(), name ='login'),
    path('push/',views.Push, name ='push'),
    path('logout/',views.Logout, name ='logout'),
    path('createpage/',views.create, name ='createpage'),
    path('updatepage/<str:pk>/',views.update, name ='updatepage'),
    path('delete/<str:pk>/',views.delete, name ='delete'),
    path('topic/', views.Topic, name ='topic'),
    path('addtopic/', views.AddTopic, name ='addtopic'),
    path('updatetopic/<str:pk>/',views.updatetopic, name ='updatetopic'),
    path('deletetopic/<str:pk>/',views.deletetopic, name ='deletetopic'),
]
